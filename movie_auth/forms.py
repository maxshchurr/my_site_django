from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
import datetime

from .models import Site_User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=255)
    dob = forms.DateField(label='Date of birth', required=True, initial=datetime.date.today, widget=forms.DateInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Site_User

        fields = ('username', 'email', 'dob', 'password')


class LoginForm(forms.ModelForm):


    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Site_User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid username or password')