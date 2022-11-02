from django import forms
from django.forms import ModelForm, Textarea, widgets
from django.contrib.auth.models import User
#from captcha.fields import ReCaptchaField
from .models import Evento


class EventForm(ModelForm):
    #captcha = ReCaptchaField()
    date_start = forms.DateTimeField(input_formats = ['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={'class':'form-control form-control-lg','type':'datetime-local'}))
    date_end = forms.DateTimeField(input_formats = ['%d/%m/%Y'], widget=forms.DateTimeInput(attrs={'class':'form-control form-control-lg','type':'datetime-local'}))

    class Meta:
        model = Evento
        fields = ['title', 'body', 'web', 'city', 'state', 'country', 'longitud', 'latitud'
        , 'location', 'organiza', 'date_start', 'date_end', 'picture', 'banner', 'flayer', 'user']
        widgets = {
            'body': Textarea(attrs={'rows':5, 'cols':45}),
        }
