
from dataclasses import fields
import filecmp
from django import forms
from django .contrib. auth.forms import UserCreationForm,PasswordChangeForm, PasswordResetForm, UserChangeForm
from django.contrib.auth.models import User

class UserCreatingForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email', )
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    
    class Meta:
        model = User 
        fields = ('old_password', 'new_password1', 'new_password2')

class PasswordResetForm(PasswordResetForm):
    
    class Meta:
        model = User 
        
        
class ChangeDetailsForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    
