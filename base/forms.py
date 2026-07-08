from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .validators import custom_authentication_password,duplicate_email,duplicate_username
from django.contrib.auth.forms import AuthenticationForm

from .models import Image

class RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(max_length=50, widget=(forms.PasswordInput(attrs={"placeholder":"Re-Enter","class":"form-control"})))
    password=forms.CharField(max_length=50,validators=[custom_authentication_password] ,widget=(forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"})))
    username=forms.CharField(max_length=50,validators=[duplicate_username], widget=(forms.TextInput(attrs={"placeholder":"Username","class":"form-control"})))
    email=forms.EmailField(max_length=50,validators=[duplicate_email], widget=(forms.EmailInput(attrs={"placeholder":"Exemple@gmail.com","class":"form-control"})))


    class Meta:
        model=User

        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={
                "placeholder":"First Name",
                "class":"form-control"
            }),
            "last_name":forms.TextInput(attrs={
                "placeholder":"Last Name",
                "class":"form-control"
            }),
            
        }

    def clean(self):
        cleaned_data=super().clean()
        pwd=cleaned_data.get("password")
        cpwd=cleaned_data.get("confirm_password")

        if pwd:
            try:
                validate_password(pwd)
            except ValidationError as e:
                raise forms.ValidationError(e.message)
            
        if pwd!=cpwd:
            raise forms.ValidationError("Password must be same...")

        
class CustomAuthenticationForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Username","class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"}))



class ImageForm(forms.ModelForm):

    class Meta:

        model=Image
        fields=["title","description","catagory","image_path"]
        widgets={
            "title":forms.TextInput(attrs={
                "placeholder":"Enter Image Title",
                "class":"form-control"
            }),
            "description":forms.Textarea(attrs={
                "placeholder":"Enter Image Description",
                "class":"form-control",
                "rows":"4"
            }),
            "catagory":forms.Select(attrs={
                "class":"form-control"
            }),
            "image_path":forms.FileInput(attrs={
                "class":"form-control"
            })
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=["title","description","catagory"]
        widgets={
            "title":forms.TextInput(attrs={
                "placeholder":"Enter Image Title",
                "class":"form-control"
            }),
            "description":forms.Textarea(attrs={
                "placeholder":"Enter Image Description",
                "class":"form-control",
                "rows":"4"
            }),
            "catagory":forms.Select(attrs={
                "class":"form-control"
            })
        }
