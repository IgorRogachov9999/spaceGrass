from django.urls import path
from shop.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('category/<category_slug>/', category_view, name="category_detail"),
    path('product/<product_slug>/', product_view, name="product_detail"),
    path('order/<product_slug>/', order_view, name="order_detail"),
    path('thank/<product_slug>/', thank_view, name="thank_detail"),
]
