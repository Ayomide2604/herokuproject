from django.urls import path
from.views import *

urlpatterns = [
    path('signup/', SignUpView.as_view() , name= 'signup'),
    path('password_change/', PasswordChangeView.as_view() , name= 'password_change'),
    path('password_change/success', PasswordChangeSuccessView.as_view() , name= 'password_change_success'),
    ]