from audioop import reverse
from django.shortcuts import render
from django. views. generic import CreateView
from pages.models import Product
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
class ContactView(SuccessMessageMixin,CreateView):
    model = Product
    form_class = ContactForm
    success_url = reverse_lazy('index')
    template_name = 'pages/contact.html'
    success_message = 'Your inquiry has been sent'
