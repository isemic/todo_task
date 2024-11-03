from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_task,name='add_task'),
    path('home', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/',views.add_task,name='add_task'),
] 