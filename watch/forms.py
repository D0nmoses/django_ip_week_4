from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):
    '''	
    Class to create a form for an authenticated user to create Post	
    '''
    class Meta:
        model = Post
        exclude = ['user','profile']