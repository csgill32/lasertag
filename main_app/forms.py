from django.forms import ModelForm
from django import forms
from .models import Subscriber

class Subscriber_Form(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name': forms.TextInput(attrs = {'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs = {'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs= {'placeholder': 'Email Address'})
        }