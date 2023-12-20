from django.urls import path
from myprofile import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('skill',views.handleskill,name='handleskill'),
    path('resume/', views.resume,name='resume'),
]
