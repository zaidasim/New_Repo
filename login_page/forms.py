# forms.py
from django import forms
from .models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class CreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','text']



class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email']
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
