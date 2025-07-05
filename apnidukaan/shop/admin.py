from itertools import product
from unicodedata import category
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Categories, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name' , 'product_price' , 'product_stock' , 'product_brand']
    search_fields = ['product_name', 'product_category' , 'product_uploadDate', 'product_brand']
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    search_fields = ['category_name']

default_auto_field = 'django.db.models.BigAutoField'  # type: ignore