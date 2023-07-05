from django.db import models

# Create your models here.
class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class hobbyname_tb(models.Model):
    hobbyname=models.CharField(max_length=20)

class hobbyfactor_tb(models.Model):
    factor=models.CharField(max_length=20)
    hobbyid=models.ForeignKey(hobbyname_tb,on_delete=models.CASCADE)

class season_tb(models.Model):
    seasonname=models.CharField(max_length=20)

class seasonfactor_tb(models.Model):
    factor=models.CharField(max_length=20)
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)

class seasoncountry_tb(models.Model):
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    countryid=models.ForeignKey("user.country_tb",on_delete=models.CASCADE)
    stateid=models.ForeignKey("user.state_tb",on_delete=models.CASCADE)
    factorid=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
    month=models.IntegerField()

class agefactor_tb(models.Model):
    minimumage=models.IntegerField()
    maximumage=models.IntegerField()
    factor=models.CharField(max_length=20)