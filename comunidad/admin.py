from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'sharePhone', 'city', 'state', 'country')


class ComunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'encargado', 'phone', 'email', 'city', 'state', 'country')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'encargado', 'phone', 'email', 'city', 'state', 'country')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comunity, ComunityAdmin)
admin.site.register(Company, CompanyAdmin)
