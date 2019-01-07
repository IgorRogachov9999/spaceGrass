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