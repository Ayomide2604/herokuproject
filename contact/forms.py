from django.forms import ModelForm
from . models import Contact
from django import forms

class ContactForm(ModelForm):
    first_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control',}))
    last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control',}))
    email = forms.EmailField(max_length=255,widget=forms.EmailInput(attrs={'class': 'form-control',}))
    phone = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class': 'form-control',}))
    subject = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class': 'form-control',}))
    message = forms.Textarea(attrs={'class': 'form-control',})


    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'subject', 'message',)

