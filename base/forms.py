from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(max_length=50, widget=(forms.PasswordInput(attrs={"placeholder":"Re-Enter"})))
    class Meta:
        model=User

        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={
                "placeholder":"First Name",
            }),
            "last_name":forms.TextInput(attrs={
                "placeholder":"Last Name",
            }),
            "username":forms.TextInput(attrs={
                "placeholder":"Username",
            }),
            "email":forms.EmailInput(attrs={
                "placeholder":"exemple@gmail.com",
            }),
            "password":forms.PasswordInput(attrs={
                "placeholder":"Enter password ",
            })
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

        
