from django.urls import path
from.views import *

urlpatterns = [
    path('', HomeView.as_view(), name= 'index'),
    path('products/', ProductView.as_view(), name= 'products'),
    #path('<slug:slug>', DetailView.as_view(), name= 'product')

]

