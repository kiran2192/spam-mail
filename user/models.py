from django.db import models

# Create your models here.
class country_tb(models.Model):
    country=models.CharField(max_length=20)

class state_tb(models.Model):
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    state=models.CharField(max_length=20)

class register_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    stateid=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    securityquestion=models.CharField(max_length=20,default="abc")
    answer=models.CharField(max_length=20,default="abc")

class hobby_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    hobbyid=models.ForeignKey("siteadmin.hobbyname_tb",on_delete=models.CASCADE)

class message_tb(models.Model):
    senderid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name="sender")
    receiverid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name="receiver")
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="pending")
    filterstatus=models.CharField(max_length=20,default="pending")

class trash_tb(models.Model):
    messageid=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)

class contact_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name="user")
    contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name="contact")
    name=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)

class blacklist_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name="user1")
    contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name="contact1")
    name=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)

class customerhobbyfactor_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    hobbyid=models.ForeignKey("siteadmin.hobbyname_tb",on_delete=models.CASCADE)
    factorid=models.ForeignKey("siteadmin.hobbyfactor_tb",on_delete=models.CASCADE)

class customeragefactor_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey("siteadmin.agefactor_tb",on_delete=models.CASCADE)

class customerseasoncountry_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey("siteadmin.seasonfactor_tb",on_delete=models.CASCADE)