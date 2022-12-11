from django.db import models

class member(models.Model):
    gender_coice=(('M', 'Male'),
                      ('F', 'Female'),
                     )
    batch=(
        ('M1' , '6-7 AM'),
        ('M2' , '7-8 AM'),
        ('M3' , '8-9 AM'),
        ('N1' , '5-6 PM')
    )
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,null=True,blank=True)
    phone_no=models.CharField(max_length=10,blank=True,null=True)
    gender = models.CharField(max_length=1, choices=gender_coice,blank=True,null=True)
    schedule_preference=models.CharField(max_length=2 , choices=batch,blank=True,null=True)
    age=models.IntegerField(max_length=2,blank=True,null=True)
    upi_id=models.CharField(max_length=20,blank=True,null=True)
    amount=models.IntegerField(max_length=3,blank=True,null=True)
    date=models.DateField()
    













# Create your models here.
