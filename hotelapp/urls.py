from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
   
    path('staff_register/',views.staff_register,name="staff_register"),
    path('staff_login/',views.staff_login,name="staff_login"),
    path('staff_userlog/',views.staff_userlog,name="staff_userlog"),
    path('staff_profile',views.staff_profile,name="staff_profile"),
    path('staff_update/<str:pk>',views.staff_update,name="staff_update"),
    path('staff_delete/<str:pk>',views.staff_delete,name="staff_delete"),
    path('staff_logout/',views.staff_logout,name="staff_logout"),
    path('staff_updateview/',views.staff_updateview,name="staff_updateview"),

    path('customer_register/',views.customer_register,name="customer_register"),
    path('customer_login/',views.customer_login,name="customer_login"),
    path('customer_userlog/',views.customer_userlog,name="customer_userlog"),
    path('customer_profile/',views.customer_profile,name="customer_profile"),
    path('customer_update/<str:pk>',views.customer_update,name="customer_update"),
    path('customer_delete/<str:pk>',views.customer_delete,name="customer_delete"),
    path('customer_logout/',views.customer_logout,name="customer_logout"),
    
    path('addrooms/',views.addrooms,name="addrooms"),
    path('room_update/<str:pk>',views.room_update,name="room_update"),
    path('check/',views.check,name="check"),
    path('rooms/',views.rooms,name="rooms"),
    path('booking/',views.booking,name="booking"),
    path('room_approve/<str:pk>',views.room_approve,name="room_approve"),
]