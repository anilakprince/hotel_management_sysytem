from django.shortcuts import render,redirect
from .forms import AddStaffForm,AddCustomerForm,AddRoomForm,BookingForm
from .models import Staff,Customers,Room,Booking
from django.contrib.auth import authenticate,login as log,logout
from django.contrib.auth.models import User,auth
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")

def staff_register(request):
    form = AddStaffForm()
    if request.method =="POST":
        form = AddStaffForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_login')
    return render(request,"staff_register.html",{'form':form})

def staff_login(request):
    return render(request,"staff_login.html")

def staff_userlog(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        sr= Staff.objects.filter(username=username,password=password,approval=True)
        if sr:
            staff_details=Staff.objects.get(username=username,password=password)
            id=staff_details.id
            username=staff_details.username
            mobile_number=staff_details.mobile_number
            
            request.session['id']=id
            request.session['username']=username
            request.session['mobile_number']=mobile_number
            return redirect('staff_profile')
        else:
            ce='Invalid login or request not approved'
            return render(request,'staff_login.html',{'ce':ce})
    else:
        return render(request,'staff_register.html') 

def staff_profile(request):
    id=request.session['id']
    username=request.session['username']
    profile=Staff.objects.get(pk=id)
    return render(request,"staff_profile.html",{'username':username,'profile':profile,'id':id})

def staff_update(request,pk):
    sr=Staff.objects.get(id=pk)
    form= AddStaffForm(instance = sr)
    if request.method=="POST":
        form=AddStaffForm(request.POST,instance=sr)
        if form.is_valid:
            form.save()
            return redirect("staff_profile")
        return render(request,"staff_update.htm",{'form':form}) 

def staff_delete(request,pk):
    sr=Staff.objects.get(id=pk)
    sr.delete()
    return redirect(staff_login)            
    
def staff_logout(request):
    logout(request)
    return redirect("staff_login")



def customer_register(request):
    form = AddCustomerForm()
    if request.method =="POST":
        form = AddCustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_login')
    return render(request,"customer_register.html",{'form':form})

def customer_login(request):
    return render(request,"customer_login.html")

def customer_userlog(request):
    if request.method=='POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        cr= Customers.objects.filter(name=name,mobile_number=mobile_number)
        if cr:
            customer_details=Customers.objects.get(name=name,mobile_number=mobile_number)
            id=customer_details.id
            name=customer_details.name
            mobile_number=customer_details.mobile_number
            request.session['id']=id
            request.session['name']=name
            request.session['mobile_number']=mobile_number
            
            return redirect('customer_profile')
        else:
            ce='Invalid login'
            return render(request,'customer_login.html',{'ce':ce})
    else:
        return render(request,'customer_register.html')    
def customer_profile(request):
    id=request.session['id']
    name=request.session['name']
    mobile_number=request.session['mobile_number']
    profile=Customers.objects.get(pk=id)
    return render(request,"customer_profile.html",{'name':name,'mobile_number':mobile_number,'profile':profile,'id':id})

def customer_update(request,pk):
    cu = Customers.objects.get(id=pk)
    form = AddCustomerForm(instance = cu)
    if request.method =="POST":
        form = AddCustomerForm(request.POST,instance = cu)
        if form.is_valid():
            form.save()
            return redirect("customer_profile") 
    return render(request,"customer_update.html",{'form':form})

def customer_delete(request,pk):
    cr=Customers.objects.get(id=pk)
    cr.delete()
    return redirect("customer_login")

def customer_logout(request):
    logout(request)
    return redirect("customer_login")

def addrooms(request):
    form = AddRoomForm()
    if request.method =="POST":
        form = AddRoomForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_profile')
    return render(request,"addrooms.html",{'form':form})
def staff_updateview(request):
    rr=Room.objects.all()
    return render(request,"staff_updateview.html",{'rr':rr}) 

def room_update(request,pk):
    rr=Room.objects.get(id=pk)
    form = AddRoomForm(instance = rr)
    if request.method=="POST":
        form = AddRoomForm(request.POST,instance = rr)
        if form.is_valid:
            form.save()
            return redirect("staff_profile")
    return render(request,"room_update.html",{'form':form})   

def check(request):
    rr=Booking.objects.all()
    return render(request,"check.html",{'rr':rr})

def rooms(request):
    rr=Room.objects.all()
    return render(request,"rooms.html",{'rr':rr})

def booking(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        room_id = request.POST.get('room_id')
        checkin_date = datetime.strptime(request.POST.get('checkin_date'), '%Y-%m-%d').date()
        checkout_date = datetime.strptime(request.POST.get('checkout_date'), '%Y-%m-%d').date()
        customer = Customers.objects.get(id=customer_id)
        room = Room.objects.get(id=room_id)
        booking = Booking.objects.create(customer=customer, room=room, checkin_date=checkin_date, checkout_date=checkout_date)

        room.availability = False
        room.save()
        return redirect('rooms')
    else:
        customers = Customers.objects.all()
        rooms = Room.objects.filter(availability=True)
        return render(request, 'booking.html', {'customers': customers, 'rooms': rooms})
    

def room_approve(request,pk):
    ru=Booking.objects.get(id=pk)
    form = BookingForm(instance = ru)
    if request.method=="POST":
        form = BookingForm(request.POST,instance=ru)
        if form.is_valid:
            form.save()
            return redirect("check")
    return render(request,"room_approve.html",{'form':form})   
    