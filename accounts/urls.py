from django.urls import path
from.views import *

urlpatterns = [
    path('signup/', SignUpView.as_view() , name= 'signup'),
    path('password_change/', PasswordChangeView.as_view() , name= 'password_change'),
    path('password_change/success', PasswordChangeSuccessView.as_view() , name= 'password_change_success'),
    path('password_reset/', PasswordResetView.as_view() , name= 'password_reset_form'),
    path('dashboard/', DashboardView.as_view() , name= 'dashboard'),
    path('dashboard/change_profile/', ChangeDetailsView.as_view() , name= 'change_details'),
    ]