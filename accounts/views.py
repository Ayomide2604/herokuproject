from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView, PasswordResetView, PasswordResetCompleteView
from django.urls import reverse_lazy
from.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SignUpView(SuccessMessageMixin,CreateView):
    form_class = UserCreatingForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    success_message = 'Your account has been created successfully'
   

class PasswordChangeView(SuccessMessageMixin,PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_change_success')
    template_name = 'accounts/password_change_form.html'
    success_message = 'Your password has been changed successfully'
    

class PasswordChangeSuccessView(PasswordChangeDoneView, SuccessMessageMixin):
    template_name = ('accounts/password_change_done.html')
    success_message = 'Your password has been changed successfully'

class PasswordResetView(SuccessMessageMixin,PasswordResetView):
    form_class = PasswordResetForm
    success_message = 'Your password has been reset successfully'
    template_name = 'accounts/password_reset_form.html'

class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    success_message = 'Your password has been reset successfully'
    template_name = 'accounts/password_reset_done.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'

class ChangeDetailsView(LoginRequiredMixin,TemplateView):
    form_class = ChangeDetailsForm
    model = User
    template_name = 'accounts/change_details.html'

