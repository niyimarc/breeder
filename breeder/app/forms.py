from django import forms
from .models import Contact, Offer, Appointment, Newsletter, AnonymousContact
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

class OfferForm(forms.ModelForm):
    class Meta():
        model = Offer
        fields = ('message',)

class AppointmentForm(forms.ModelForm):
    class Meta():
        model = Appointment
        fields = ('full_name', 'email', 'phone', 'service_type', 'message')

class NewsletterForm(forms.ModelForm):
    class Meta():
        model = Newsletter
        fields = ('email',)

class AnonymousContactForm(forms.ModelForm):
    class Meta():
        model = AnonymousContact
        fields = ('full_name', 'email', 'subject', 'message')