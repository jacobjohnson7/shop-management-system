from django.urls import path
from . import views 
urlpatterns=[
    path('',views.home,name='home'),
    path('custregister',views.custregister,name='custregister'),
    path('userwelcome',views.userwelcome,name='userwelcome'),
    path('custlogin',views.custlogin,name='custlogin'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('removefromcart/<int:id>/', views.removefromcart, name='removefromcart'),
    path('payment/', views.payment, name='payment'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('viewproduct/', views.viewproduct, name='viewproduct'),
    path('updateproduct/<int:id>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:id>/', views.deleteproduct, name='deleteproduct'),
    path('logout/', views.logout, name='logout'),
    
   
   
]