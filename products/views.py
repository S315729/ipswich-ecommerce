from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category


def product_list(request):
    """Display list of all available products"""
    category_slug = request.GET.get('category')
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    """Display detailed information about a single product"""
    product = get_object_or_404(Product, slug=slug, available=True)
    
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
