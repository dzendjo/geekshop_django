from django.db import models


# Create your models here.
from django.template.defaultfilters import register


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Name', max_length=64, unique=True)
    description = models.TextField(verbose_name='Description', blank=True)

    def __str__(self):
        return self.name

    # @register.filter
    # def sort_lower(lst, key_name):
    #     return sorted(lst, key=lambda item: getattr(item, key_name).lower())

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Product name', max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    short_desc = models.CharField(verbose_name='Short description', max_length=60, blank=True)
    description = models.TextField(verbose_name='Full description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Storage', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

