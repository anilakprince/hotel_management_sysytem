from django.contrib import admin
from .models import Staff, Customers, Room,Booking
# Register your models here.
admin.site.register(Staff)
admin.site.register(Customers)
admin.site.register(Room)
admin.site.register(Booking)