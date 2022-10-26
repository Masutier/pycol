from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from PIL import Image
from django.utils import timezone


User._meta.get_field('email')._unique = True


CATEGORY = (
    ('Empresa', 'Empresa'),
    ('Fundacion', 'Fundacion'),
    ('Organizacion', 'Organizacion'),
    ('Universidad', 'Universidad')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    sharePhone = models.BooleanField(default=False)
    city = models.CharField(max_length=80, blank=True, null=True, default='Bogotá')
    state = models.CharField(max_length=80, blank=True, null=True, default='Bogotá D.C.')
    country = models.CharField(max_length=80, blank=True, null=True, default='Colombia')
    summary = models.CharField(max_length=1600, blank=True, null=True)
    information = models.TextField(null=False, blank=False)
    github = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    slack = models.CharField(max_length=100, blank=True, null=True)
    googlePlus = models.CharField(max_length=100, blank=True, null=True)
    medium = models.CharField(max_length=100, blank=True, null=True)
    meetup = models.CharField(max_length=100, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(auto_now_add=True,)
    image = ResizedImageField(size=[300, 300], upload_to='pythonistas', blank=True, null=True, default='pythonistas/default.png')

    def __str__(self):
        return f'{self.user.username} Profile'


    def get_people_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})


class Comunity(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    encargado = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    summary = models.CharField(max_length=1600, blank=True, null=True)
    information = models.TextField(null=False, blank=False)
    longitud = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    latitud = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True, default='Bogotá')
    state = models.CharField(max_length=80, blank=True, null=True, default='Bogotá D.C.')
    country = models.CharField(max_length=80, blank=True, null=True, default='Colombia')
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    slack = models.CharField(max_length=100, null=True, blank=True)
    googlePlus = models.CharField(max_length=100, null=True, blank=True)
    medium = models.CharField(max_length=100, null=True, blank=True)
    meetup = models.CharField(max_length=100, null=True, blank=True)
    web = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(auto_now_add=True,)
    Logo = ResizedImageField(size=[300, 300], upload_to='communities', blank=True, null=True, default='communities/logoDefault.png')
    image = ResizedImageField(size=[800, 600], upload_to='communities', blank=True, null=True, default='communities/default.png')

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("comunityProfile", kwargs={"pk": self.pk})


class Company(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    encargado = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    summary = models.CharField(max_length=1600, blank=True, null=True)
    information = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=50, blank=True, null=True, default='Empresa', choices=CATEGORY)
    longitud = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    latitud = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True, default='Bogotá')
    state = models.CharField(max_length=80, blank=True, null=True, default='Bogotá D.C.')
    country = models.CharField(max_length=80, blank=True, null=True, default='Colombia')
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    slack = models.CharField(max_length=100, null=True, blank=True)
    googlePlus = models.CharField(max_length=100, null=True, blank=True)
    medium = models.CharField(max_length=100, null=True, blank=True)
    meetup = models.CharField(max_length=100, null=True, blank=True)
    web = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(auto_now_add=True,)
    Logo = models.ImageField(default='media/companies/default.png', upload_to='img/companies')
    image = models.ImageField(default='media/companies/default.png', upload_to='img/companies')

    def __str__(self):
        return self.name


    def get_people_absolute_url(self):
        return reverse("company", kwargs={"pk": self.pk})
