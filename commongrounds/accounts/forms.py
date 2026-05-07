from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserAndProfileCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    display_name = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "display_name", "email", "password1", "password2")