from django.shortcuts import render
from products.models import Product, Category

def home(request):
    """Home page showing featured products"""
    featured_products = Product.objects.filter(available=True)[:8]
    categories = Category.objects.all()
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'home.html', context)
