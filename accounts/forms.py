from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'phone_number', 'id_number',
            'address', 'id_copy', 'proof_of_address', 'email', 'password1',
            'password2'
        ]

        widgets = {
            'username':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'first_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@thuso.com'
            }),
            'password1':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            'password2':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            'phone_number':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'id_number':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Number'
            }),
            'address':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'address'
            }),
        }


class UpdateCustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'phone_number', 'id_number', 'address',
            'id_copy', 'proof_of_address', 'email'
        ]