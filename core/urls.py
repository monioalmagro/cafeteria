from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.home, name="about"),
    path('services', views.home, name="services"),
    path('store', views.home, name="store"),
    path('contact', views.home, name="contact"),
    path('blog', views.home, name="blog"),
    
]
