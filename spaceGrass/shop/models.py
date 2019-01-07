from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

class Grass(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)
    grass = models.ForeignKey(Grass, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    location = models.CharField(max_length=256)
    
    def __str__(self):
        return self.location
 
class Payment(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return str(self.id)

