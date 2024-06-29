from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=50, label='Email', help_text='Required')
    first_name = forms.CharField(required=True, max_length=50, label='First name', help_text='Required')
    last_name = forms.CharField(required=True, max_length=50, label='Last name', help_text='Required')
    age = forms.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email", 'first_name', 'last_name', 'age')