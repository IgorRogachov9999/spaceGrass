from django.shortcuts import render
from shop.models import Category, Product

# Create your views here.

def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'index.html', context)

def product_view(request, product_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
        'categories': categories,
    }

    return render(request, 'product.html', context=context)

def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    products = Product.objects.all()
    product_of_category = []

    for product in products:
        if product.grass.category == category:
            product_of_category.append(product)

    context = {
        'category': category,
        'products_of_category': product_of_category,
        'categories': categories,
    }

    return render(request, 'category.html', context=context)