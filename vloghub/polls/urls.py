from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("Profile_list/",views.ProfileList,name="Profile_list"),
    path('login/',views.Login,name= "Login"),
    path('Profile/<int:pk>',views.ViewProfile,name= 'Profile'),
    path('My_profile/',views.MyProfile,name = 'MyProfile'),
    path("f.q.a/",views.FQA,name='FQA'),
    path('contact/',views.contact,name='contact'),
    path('logout',views.Logout,name='logout'),
    path('register/',views.Register,name='register'),
    path('vlog_like/<int:pk>',views.vlog_like,name='like'),
    path('vlog_share/<int:pk>',views.vlog_share,name='share'),
    path('unfollow/<int:pk>',views.unfollow,name="unfollow"),
    path('follow/<int:pk>',views.follow,name="follow"),
    path('sreached/',views.sreach,name='sreach'),
    path("delete/<int:pk>",views.delete_vlog,name="delete"),
    path("update/<int:pk>",views.update_vlog,name="update")
]
