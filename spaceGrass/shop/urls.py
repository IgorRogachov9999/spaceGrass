from django.urls import path
from shop.views import *

urlpatterns = [
    path('', home_view, name='home'),
]
