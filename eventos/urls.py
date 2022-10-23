from django.urls import path, include
from .views import *


urlpatterns = [
    path('eventos', eventos, name='eventos'),
    path('crearEvento', crearEvento, name='crearEvento'),
    path('eventDetail/<int:pk>', eventDetail, name='eventDetail'),
]

