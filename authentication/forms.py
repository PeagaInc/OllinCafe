# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class"       : "form-control",
                "oninvalid"   : "this.setCustomValidity('Please enter user name')", 
                "oninput"     : "setCustomValidity('')"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",          
                "class"       : "form-control",
                "oninvalid"   : "this.setCustomValidity('Please enter your password')", 
                "oninput"     : "setCustomValidity('')"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email')
