from django.contrib import admin
from mainapp.models import Product
from mainapp.models import ProductCategory

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
