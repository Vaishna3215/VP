from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.sign,name='sign'),
    path('newlogin/',views.newlogin,name='newlogin'),
    path('indexe/',views.indexe,name='indexe'),
    path('register/',views.register,name='register'),
    path('loginadmin/',views.loginadmin,name='loginadmin'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('employee/',views.employee,name='employee'),
]