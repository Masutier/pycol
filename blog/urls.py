from django.urls import path, include
from .views import *


urlpatterns = [
    path('blog', blog, name='blog'),
    path('blog<slug:slug>', blogDetail, name='blogDetail'),
]

