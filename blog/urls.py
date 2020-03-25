
from django.urls import path

from django.conf import settings


urlpatterns = [
    path('',views.blog,name="blog"),
    
]
