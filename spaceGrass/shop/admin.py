from django.contrib import admin
from shop.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Grass)
admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.register(Order)