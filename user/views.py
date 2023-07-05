from django.shortcuts import render,redirect
from siteadmin.models import *
from user.models import *
import datetime

from django.http import JsonResponse


# Create your views here.
def register(request):
    country=country_tb.objects.all()
    hobby=hobbyname_tb.objects.all()
    return render(request,'register.html',{'con':country,'hby':hobby})

def getstate(request):
    ste=request.GET['co']
    state=state_tb.objects.filter(countryid_id=ste)
    return render(request,'getstate.html',{'st':state})

def registeraction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    dob=request.POST['dob']
    username=request.POST['username']
    password=request.POST['password']
    country=request.POST['country']
    state=request.POST['state']
    squestion=request.POST['question']
    answer=request.POST['answer']
    box=request.POST.getlist('checkbox')
    user=register_tb(name=name,address=address,gender=gender,phone=phone,dob=dob,username=username+'@mymail.com',password=password,countryid_id=country,stateid_id=state,securityquestion=squestion,answer=answer)
    user.save()
    for bid in box:
        hobby=hobbyname_tb.objects.get(id=bid)
        hb=hobby_tb(userid_id=user.id,hobbyid_id=bid)
        hb.save()
    
    return redirect('index')

def sendmessage(request):
    return render(request,'message.html')

def checkreceivername(request):
        receiver=request.GET['rcvr']
        user=register_tb.objects.filter(username=receiver)

        if(len(user)>0):
            msg="exist"
            
        else:
            msg="not exist"
        return JsonResponse({'valid':msg})

def sendmessageaction(request):
    sender=request.session['id']
    rec=request.POST['receivername']
    rid=register_tb.objects.get(username=rec)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    
    smg=message_tb(senderid_id=sender,receiverid=rid,subject=subject,message=message,date=date,time=time)
    smg.save()
    return redirect('sendmessage')

def viewsendmessage(request):
    sender=request.session['id']
    status=["pending","deleted by receiver"]
    vm=message_tb.objects.filter(senderid_id=sender,status__in=status)
    return render(request,'viewsendmessage.html',{'vsmg':vm})

def deletemsg(request,id):
    vmsg=message_tb.objects.filter(id=id)
    status=vmsg[0].status
    if(status=="deleted by receiver"):
        de=message_tb.objects.filter(id=id).delete()
        return redirect('viewsendmessage')
    if(status=="pending"):
        
        dl=message_tb.objects.filter(id=id).update(status="deleted by sender")
    return redirect('viewsendmessage')

def inbox(request):
    receiver=request.session['id']
    status=["deleted by sender","pending"]
    #before applying filter
    #inbx=message_tb.objects.filter(receiverid_id=receiver).exclude(id__in=trash_tb.objects.filter(userid_id=receiver))

    #after applying filter
    age=customeragefactor_tb.objects.filter(userid_id=receiver)
    for a in age:
        msg=message_tb.objects.filter(receiverid_id=receiver,filterstatus="pending",message__icontains=a.factorid.factor).exclude(senderid__in=blacklist_tb.objects.filter(userid=receiver).values('contactid')).update(filterstatus="filtered")
        
    cust=customerhobbyfactor_tb.objects.filter(userid_id=receiver)
    for c in cust:
        hby=message_tb.objects.filter(receiverid_id=receiver,filterstatus="pending",message__icontains=c.factorid.factor).exclude(senderid__in=blacklist_tb.objects.filter(userid=receiver).values('contactid')).update(filterstatus="filtered")
        
    season=customerseasoncountry_tb.objects.filter(userid_id=receiver)
    for s in season:
        sea=message_tb.objects.filter(receiverid_id=receiver,filterstatus="pending",message__icontains=s.factorid.factor).exclude(senderid__in=blacklist_tb.objects.filter(userid=receiver).values('contactid')).update(filterstatus="filtered")
        
    contact=contact_tb.objects.filter(userid=receiver)
    for c in contact:
        cn=message_tb.objects.filter(receiverid=receiver,filterstatus="pending",senderid=c.contactid).update(filterstatus="filtered")
    inbx=message_tb.objects.filter(receiverid=receiver,status__in=status,filterstatus="filtered").exclude(id__in=trash_tb.objects.filter(userid=receiver).values('messageid_id'))
    return render(request,'inbox.html',{'inb':inbx})



def movetotrash(request):
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    box=request.POST.getlist('checkbox')
    receiver=request.session['id']
    status=["deleted by sender","pending"]
    for mid in box:
        m=message_tb.objects.get(id=mid)
        trash=trash_tb(userid_id=request.session['id'],messageid=m,date=date,time=time)
        trash.save()
        inbx=message_tb.objects.filter(receiverid=receiver,status__in=status,filterstatus="filtered").exclude(id__in=trash_tb.objects.filter(userid=receiver).values('messageid_id'))
        return render(request,'inbox.html')

def viewtrash(request):
    receiver=request.session['id']
    tr=trash_tb.objects.filter(userid_id=receiver)
    return render(request,'viewtrash.html',{'tsh':tr})

def delmsg(request,id):
    t=trash_tb.objects.filter(id=id)
    m=message_tb.objects.filter(id=t[0].messageid_id)
    x=m[0].status
    if (x=="pending"):
        up=message_tb.objects.filter(id=t[0].messageid_id).update(status="deleted by receiver")
        d=trash_tb.objects.filter(id=id).delete()
    return redirect('viewtrash')

def forwardmsg(request,id):
    m=message_tb.objects.filter(id=id)
    return render(request,'forwardmsg.html',{'fwd':m})

def forwardmsgaction(request):
    sender=request.session['id']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    subject=request.POST['subject']
    message=request.POST['message']
    rec=request.POST['receivername']
    rid=register_tb.objects.get(username=rec)
  

    m=message_tb(date=date,time=time,subject=subject,message=message,senderid_id=sender,receiverid=rid,status="forwarded message")
    m.save()
    return redirect('inbox')

def replymsg(request,id):
    m=message_tb.objects.filter(id=id)
    return render(request,'replymsg.html',{'rp':m})

def replymsgaction(request):
    sender=request.session['id']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    subject=request.POST['subject']
    message=request.POST['message']
    rec=request.POST['receivername']
    rid=register_tb.objects.get(username=rec)
  

    m=message_tb(date=date,time=time,subject=subject,message=message,senderid_id=sender,receiverid=rid,status="reply")
    m.save()
    return redirect('inbox')

def contact(request):
    return render(request,'contact.html')

def checkcntct(request):
    c=request.GET['cnt']
    cc=register_tb.objects.filter(username=c)

    if(len(cc)>0):
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})

def contactaction(request):
    user=request.session['id']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    contact=request.POST['contact']
    cn=register_tb.objects.get(username=contact)
    name=request.POST['name']
    remarks=request.POST['remarks']

    cntct=contact_tb(contactid=cn,userid_id=user,date=date,time=time,remarks=remarks,name=name)
    cntct.save()
    return render(request,'userhome.html')

def viewcontact(request):
    user=request.session['id']
    v=contact_tb.objects.filter(userid_id=user)
    return render(request,'viewcontact.html',{'vc':v})

def delcontact(request,id):
    c=contact_tb.objects.filter(id=id).delete()
    return redirect('viewcontact')

def blacklist(request):
    return render(request,'blacklist.html')

def blacklistaction(request):
    user=request.session['id']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    name=request.POST['name']
    remarks=request.POST['remarks']
    contact=request.POST['contact']
    c=register_tb.objects.get(username=contact)

    b=blacklist_tb(name=name,remarks=remarks,userid_id=user,contactid=c,date=date,time=time)
    b.save()
    return render(request,'userhome.html')

def viewblacklist(request):
    user=request.session['id']
    b=blacklist_tb.objects.filter(userid_id=user)
    return render(request,'viewblacklist.html',{'bl':b})

def delblcklist(request,id):
    d=blacklist_tb.objects.filter(id=id).delete()
    return redirect('viewblacklist')

def movetoblacklist(request,id):
    user=request.session['id']
    cntct=contact_tb.objects.filter(id=id)
    n=cntct[0].name
    r=cntct[0].remarks
    c=cntct[0].contactid
   
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    
    bl=blacklist_tb(contactid=c,userid_id=user,date=date,time=time,name=n,remarks=r)
    bl.save()
    cntct.delete()
    return redirect('viewcontact')

def customerhobby(request):
    user=request.session['id']
    h=hobby_tb.objects.filter(userid=user)
    return render(request,'customerhobby.html',{'hby':h})

def getfctr(request):
    h=request.GET['hbby']
    hb=hobbyfactor_tb.objects.filter(hobbyid=h)
    return render(request,'getfctr.html',{'hh':hb})

def customerhobbyaction(request):
    user=request.session['id']
    hid=request.POST['hobby']
    fid=request.POST['hobbyfactor']

    cu=customerhobbyfactor_tb(userid_id=user,hobbyid_id=hid,factorid_id=fid)
    cu.save()
    return render(request,'userhome.html')

def customeragefactor(request):
    user=request.session['id']
    r=register_tb.objects.filter(id=user)
    byear=r[0].dob
    y=byear.split('-')
    birthyear=y[0]
    dte=datetime.date.today()
    currentyear=dte.year
    age=int(currentyear)-int(birthyear)
    print(age)
    fr=agefactor_tb.objects.filter(minimumage__lte=age,maximumage__gte=age)
    return render(request,'customerage.html',{'fctr':fr})

def customeragefactoraction(request):
    user=request.session['id']
    factor=request.POST['agefactor']
    cu=customeragefactor_tb(userid_id=user,factorid_id=factor)
    cu.save()
    return render(request,'userhome.html')


def cseasoncountry(request):
    user=request.session['id']
    r=register_tb.objects.filter(id=user)
    country=r[0].countryid_id
    print(country)
    state=r[0].stateid_id
    print(state)
    dte=datetime.date.today()
    month=dte.month
    print(month)
    f=seasoncountry_tb.objects.filter(month=month,countryid_id=country,stateid_id=state)
    print(f)
    return render(request,'csfactor.html',{'csf':f})

def cscountryaction(request):
    user=request.session['id']
    factor=request.POST['seasonfactor']
    csc=customerseasoncountry_tb(userid_id=user,factorid_id=factor)
    csc.save()
    return render(request,'userhome.html')

def viewspam(request):
    user=request.session['id']
    status=["pending","deleted by sender"]
    m=message_tb.objects.filter(filterstatus="pending",status__in=status,receiverid_id=user)
    return render(request,'viewspam.html',{'vs':m})

def delspam(request,id):
    m=message_tb.objects.filter(id=id)
    st=m[0].status

    if st=="deleted by sender":
        ms=message_tb.objects.filter(id=id).delete()

    if st=="pending":
        mg=message_tb.objects.filter(id=id).update(status="deleted by receiver")
    return redirect('viewspam')

def updateprofile(request):
    user=request.session['id']
    retb=register_tb.objects.filter(id=user)
    cntb=country_tb.objects.all()
    hbntb=hobbyname_tb.objects.all()
    hbtb=hobby_tb.objects.filter(userid_id=user)
    return render(request,'updateprofile.html',{'cn':cntb,'hbn':hbntb,'hb':hbtb,'re':retb})

def updateprofileaction(request):
    user=request.session['id']
    u=register_tb.objects.get(id=user)
    n=request.POST['name']
    a=request.POST['address']
    g=request.POST['gender']
    p=request.POST['phone']
    dob=request.POST['dob']
    c=request.POST['country']
    s=request.POST['state']
    an=request.POST['answer']
    se=request.POST['securityquestion']
    us=request.POST['username']
    pswd=request.POST['password']
    reg=register_tb.objects.filter(id=user).update(name=n,address=a,gender=g,phone=p,dob=dob,countryid_id=c,stateid_id=s,answer=an,securityquestion=se,username=us,password=pswd)
    
    hby=request.POST.getlist('checkbox')
    h=hobby_tb.objects.filter(userid_id=user).delete()
    for c in hby:
        hh=hobbyname_tb.objects.get(id=c)
        hb=hobby_tb(userid=u,hobbyid=hh)
        hb.save()
    return render(request,'userhome.html')

def logout(request):
    request.session.flush()
    return redirect('index')


   
   

     
   
