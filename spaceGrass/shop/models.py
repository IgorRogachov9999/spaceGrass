from django.db import models
from django.urls import reverse
from transliterate import translit
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.category.slug, filename)

def pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(translit(instance.name, reversed=True))

class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)

class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

class Grass(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to=image_folder)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)
    grass = models.ForeignKey(Grass, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    count = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

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
    email = models.EmailField()

    def __str__(self):
        return str(self.id)

pre_save.connect(pre_save_slug, sender=Category)
pre_save.connect(pre_save_slug, sender=Product)
pre_save.connect(pre_save_slug, sender=Grass)