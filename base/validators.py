from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms 
import re


def duplicate_username(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError("Username already exists")
    else:
        return value
    
def duplicate_email(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError("Email already exists")
    else:
        return value
    

def custom_authentication_password(value):
    if not re.search(r"[0-9]",value):
        raise forms.ValidationError("Password Must have atleast one number")
    
    if not re.search(r'[A-Z]',value):
        raise forms.ValidationError("Password Must have atleast one capital letter")
    
    if not re.search(r"[!@#$%^&*]",value):
        raise forms.ValidationError("Password Must have atleast one Special Character")
