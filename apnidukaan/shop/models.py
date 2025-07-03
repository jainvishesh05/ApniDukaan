from enum import unique
from tabnanny import verbose
from turtle import mode
from unicodedata import category
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10 , decimal_places=2, default=0.00)
    product_description = models.CharField(max_length=255 , default="no deascription")
    product_image = models.ImageField(upload_to='product_images/' ,blank = True , null=True)
    product_stock = models.IntegerField(default=0)  # type: ignore
    product_uploadDate =models.DateField(auto_now_add=True)
    product_category = models.ManyToManyField('Categories', blank=True)
    product_reviews = models.IntegerField(default=0) #type: ignore
    product_rating = models.DecimalField(max_digits=3 , decimal_places=2 , default=0.00)
    product_brand = models.CharField(max_length=50 , default="no brand")
    product_details = models.TextField(default="no details")
    product_orders = models.IntegerField(default=0) #type: ignore


    def __str__(self):
        return self.product_name

# Category model for recursive dropdowns
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_slug = models.SlugField(max_length=50 , unique=True , editable =False)
    category_image = models.ImageField(upload_to='category_images/' ,blank = True , null=True)
    category_description = models.TextField(default="no description")
    category_parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True ,related_name='subcategories')

    def __str__(self):
        return self.category_name

    def slugify_category(self):
        return slugify(self.category_name)

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = self.slugify_category()
        super().save(*args, **kwargs)

    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['category_name']


   
