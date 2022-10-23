from django.forms import ModelForm, Textarea, widgets
from django.contrib.auth.models import User
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'comm', 'body']
        widgets = {
            'body': Textarea(attrs={'rows':5, 'cols':45}),
        }

