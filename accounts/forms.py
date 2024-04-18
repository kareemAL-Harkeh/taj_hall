from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import CustomAccount

class CustomUserCreationForm(UserCreationForm) :

    class Meta(UserCreationForm) :
        
        model = CustomAccount
        fields = ('username' , 'email' ,)

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm) :
        
        model = CustomAccount
        fields = ('username' , 'email' ,)
