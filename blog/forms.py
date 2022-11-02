from django.forms import ModelForm, Textarea, widgets
from django.contrib.auth.models import User
#from captcha.fields import ReCaptchaField
from .models import Comment


class CommentForm(ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = ['user', 'comm', 'body']
        widgets = {
            'body': Textarea(attrs={'rows':5, 'cols':45}),
        }

