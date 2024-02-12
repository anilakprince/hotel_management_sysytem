from django import forms
from .models import Staff,Customers,Room,Booking

class AddStaffForm(forms.ModelForm):
    class Meta:
        model = Staff

        fields = ('staff_id','name','mobile_number','image','username','password')

        widgets = {
            'staff_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
             
        }

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customers

        fields = ('name','mobile_number','email','address','age','gender','image')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room

        fields = ('room_number','room_type','room_price')

        widgets = {
            'room_number':forms.TextInput(attrs={'class':'form-control'}),
            'room_type':forms.TextInput(attrs={'class':'form-control'}),
            'room_price':forms.TextInput(attrs={'class':'form-control'}),
            
        }    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ('customer','room','checkin_date','checkout_date')
  
        widgets = {
            'customer':forms.TextInput(attrs={'class':'form-control'}),
            'room':forms.TextInput(attrs={'class':'form-control'}),
            'checkin_date':forms.TextInput(attrs={'class':'form-control'}),
            'checkout_date':forms.TextInput(attrs={'class':'form-control'}),
            
        }    