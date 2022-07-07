from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.urls import reverse_lazy
from.forms import *
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class SignUpView(SuccessMessageMixin,CreateView):
    form_class = UserCreatingForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    success_message = 'Your account has been created successfully'
   

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_change_success')
    template_name = 'accounts/password_change_form.html'
    login_url = 'login'
    redirect_field_name = 'index'
    permission_denied_message = 'You must be logged in to change your password'


class PasswordChangeSuccessView(PasswordChangeDoneView):
    template_name = ('accounts/password_change_done.html')

