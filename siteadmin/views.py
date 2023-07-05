from django.shortcuts import render,redirect
from siteadmin.models import *
from user.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginaction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_tb.objects.filter(username=username,password=password)
    user=register_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        messages.add_message(request,messages.INFO,'Login successfull')
        return render(request,'home.html')
    elif user.count()>0:
        request.session['id']=user[0].id
        messages.add_message(request,messages.INFO,'Login successfull')
        return render(request,'userhome.html')
    else:
        return redirect('index')

def hobby(request):
    return render(request,'hobby.html')

def hobbyaction(request):
    name=request.POST['hobby']
    hby=hobbyname_tb(hobbyname=name)
    hby.save()
    return render(request,'home.html')

def hobbyfactor(request):
    hobby=hobbyname_tb.objects.all()
    return render(request,'hobbyfactor.html',{'hby':hobby})

def hobbyfactoraction(request):
    factor=request.POST['factor']
    hobby=request.POST['hobby']
    fctr=hobbyfactor_tb(factor=factor,hobbyid_id=hobby)
    fctr.save()
    messages.add_message(request,messages.INFO,'factor added')
    return redirect('hobbyfactor')

def season(request):
    return render(request,'season.html')

def seasonaction(request):
    name=request.POST['season']
    sea=season_tb(seasonname=name)
    sea.save()
    return render(request,'home.html')

def seasonfactor(request):
    sea=season_tb.objects.all()
    return render(request,'seasonfactor.html',{'ss':sea})

def sfactoraction(request):
    season=request.POST['season']
    factor=request.POST['sfactor']
    fct=seasonfactor_tb(factor=factor,seasonid_id=season)
    fct.save()
    messages.add_message(request,messages.INFO,'factor added')
    return redirect('seasonfactor')

def scountry(request):
    country=country_tb.objects.all()
    season=season_tb.objects.all()
    return render(request,'scountry.html',{'con':country,'sea':season})
    
def getstates(request):
    st=request.GET['cntry']
    state=state_tb.objects.filter(countryid_id=st)
    return render(request,'getstates.html',{'stt':state})

def getfactor(request):
    ft=request.GET['sesn']
    factor=seasonfactor_tb.objects.filter(seasonid_id=ft)
    return render(request,'getfactor.html',{'fct':factor})

def scountryaction(request):
    country=request.POST['country']
    state=request.POST['state']
    season=request.POST['season']
    factor=request.POST['factor']
    month=request.POST['month']
    scount=seasoncountry_tb(countryid_id=country,stateid_id=state,seasonid_id=season,factorid_id=factor,month=month)
    scount.save()
    return redirect('index')

def agefactor(request):
    return render(request,'agefactor.html')

def agefactoraction(request):
    minage=request.POST['minage']
    maxage=request.POST['maxage']
    factor=request.POST['factor']

    agf=agefactor_tb(minimumage=minage,maximumage=maxage,factor=factor)
    agf.save()
    return render(request,'home.html')

def forgotpassword(request):
    return render(request,'forgotpswd.html')

def forgotpasswordaction(request):
    us=request.POST['username']
    reg=register_tb.objects.filter(username=us)
    
    cntry=country_tb.objects.all()
    if reg.count()>0:
        return render(request,'newpassword.html',{'data':us,'cn':cntry})
    else:
        return render(request,'forgotpassword.html')

def newpasswordaction(request):
    usr=request.POST['username']
    cntry=request.POST['country']
    dob=request.POST['dob']
    reg=register_tb.objects.filter(username=usr,countryid_id=cntry,dob=dob)
    if reg.count()>0:
        request.session['id']=reg[0].id
        return render(request,'resetpassword.html',{'data':usr})
    else:
        return render(request,'newpassword.html')

def resetpasswordaction(request):
    user=request.session['id']
    npassword=request.POST['newpassword']
    cpassword=request.POST['confirmpassword']

    if npassword==cpassword:
        reg=register_tb.objects.filter(id=user).update(password=npassword)
        return render(request,'login.html')
    else:
        return redirect('index')
                          