from django.urls import path
from.views import *
from. import views

urlpatterns = [
    path('signuup/', SignUpView.as_view() , name= 'signup'),
    ]