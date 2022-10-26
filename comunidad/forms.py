from django import forms
from django.forms import ModelForm, Textarea, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from .models import *


class CreateUserForm(UserCreationForm):
    date_joined = forms.DateTimeField(input_formats = ['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={'class':'form-control form-control-lg','type':'datetime-local'}))
    class Meta:
        model = User
        fields = '__all__'


class ProfileForm(ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'information': Textarea(attrs={'rows':5, 'cols':45}),
        }


class ComunityForm(ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model = Comunity
        fields = '__all__'
        widgets = {
            'information': Textarea(attrs={'rows':5, 'cols':45}),
        }


class CompanyForm(ModelForm):
    
    #captcha = ReCaptchaField()
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'information': Textarea(attrs={'rows':5, 'cols':45}),
        }
