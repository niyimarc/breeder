from django import forms
from .models import Contact, Offer
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegForm(UserCreationForm):
    class Meta():
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ('subject', 'message')