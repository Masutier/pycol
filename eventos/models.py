from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from datetime import date
from django.utils import timezone


class Evento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    web = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True, default='Bogotá')
    state = models.CharField(max_length=80, blank=True, null=True, default='Bogotá D.C.')
    country = models.CharField(max_length=80, blank=True, null=True, default='Colombia')
    longitud = models.DecimalField(max_digits=17, decimal_places=14, blank=True, null=True)
    latitud = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    organiza = models.CharField(max_length=100, blank=True, null=True)
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False, blank = False, null=False)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False, blank = False, null=False)
    status = models.BooleanField(default=True)
    picture = ResizedImageField(size=[800, 600], upload_to='eventos', blank=True, null=True, default='eventos/evento.png')
    flayer = ResizedImageField(size=[1000, 1400], upload_to='eventos', blank=True, null=True, default='eventos/flayer.png')
    banner = ResizedImageField(size=[1000, 240], upload_to='eventos', blank=True, null=True, default='eventos/banner.png')
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_add']

    def __str__(self):
        return self.title

    def get_event_absolute_url(self):
        return reverse("eventDetail", kwargs={"pk": self.pk})
