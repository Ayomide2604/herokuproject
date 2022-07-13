from django.urls import path
from.views import *
from. import views


urlpatterns = [
    path('', HomeView.as_view(), name= 'index'),
    path('products/', ProductView.as_view(), name= 'products'),
    path('product/detail/<slug:slug>', views.product_detail , name= 'product'),
    path('category/detail/<slug:slug>', views.category_detail , name= 'category'),
    path('about_us', AboutView.as_view(), name= 'about_us'),
    path('cart/', views.cart, name='cart'),
    
]

