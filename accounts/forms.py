from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile



class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

        
class Profile_edit_one(forms.ModelForm):
    class Meta :
        model=User
        fields=["username","first_name","last_name","email"]
        
class Profile_edit_tow(forms.ModelForm):
    class Meta :
        model=Profile
        fields=["city","phone","image"]