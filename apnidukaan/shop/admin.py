from unicodedata import category
from django.contrib import admin

# Register your models here.
from .models import Categories, Product

admin.site.register(Product)
admin.site.register(Categories)

default_auto_field = 'django.db.models.BigAutoField'  # type: ignore