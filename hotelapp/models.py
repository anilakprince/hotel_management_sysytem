from django.db import models
from datetime import datetime

# Create your models here.
class Staff(models.Model):
    staff_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100,null=True)
    mobile_number = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Customers(models.Model):
   

    name = models.CharField(max_length=100,null=True)
    mobile_number = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
     
    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(max_length=100,null=True)
    room_type = models.CharField(max_length=100,null=True)
    room_price = models.CharField(max_length=100,null=True)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.room_number

class Booking(models.Model):
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    approval=models.BooleanField(default=False)
 
    def __str__(self):
        return self.customer.name


    

