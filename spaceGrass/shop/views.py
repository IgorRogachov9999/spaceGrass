from django.shortcuts import render
from shop.models import Category, Product, Order
from shop.forms import OrderForm

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

def order_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    form = OrderForm(request.POST or None)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'order.html', context)

def thank_view(request, product_slug):
    form = OrderForm(request.POST or None)

    if form.is_valid():
        product = Product.objects.get(slug=product_slug)
        if product.count > 0:
            email = form.cleaned_data['email']
            delivery = form.cleaned_data['delivery']
            payment = form.cleaned_data['payment']
            order = Order()
            order.email = email
            order.delivery = delivery
            order.payment = payment
            product.count -= 1
            product.save()
            order.product = product
            order.save()
            context = {
                'ansver': 'Спасибо за покупку!'
            }
        else:
            context = {
                'ansver': 'Не достаточно товара на складе!'
            }
            
        return render(request, 'thank.html', context)