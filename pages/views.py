from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,TemplateView
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Team



# Create your views here.

class HomeView(ListView):
    model = Product
    queryset = Product.objects.order_by('-date_created').filter(in_stock = True)
    template_name = 'pages/index.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductView(ListView):
    model = Product
    template_name = 'pages/products.html'
    context_object_name = 'products'
    paginate_by = 8

def product_detail(request, slug):
    products = Product.objects.order_by('-date_created').filter(in_stock = True)
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {'product': product, 'products': products}
    return render(request, 'pages/product.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.order_by('-date_created').filter(category=category, in_stock=True)
    context = {'products': products, 'category': category}

    return render(request, 'pages/category.html', context)

class AboutView(ListView):
    model = Team
    template_name = 'pages/about.html'
    context_object_name = 'team'

@login_required  
def cart(request):
    products = Product.objects.order_by('-date_created').filter(in_stock = True)
    context = {'products': products}
    return render(request, 'pages/cart.html', context)
