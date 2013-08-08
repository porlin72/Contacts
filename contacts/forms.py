from django import forms
from models import Contact
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('user')