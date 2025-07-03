from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10 , decimal_places=2, default=0.00)
    product_description = models.CharField(max_length=255 , default="no deascription")
    product_image = models.ImageField(upload_to='product_images/' ,blank = True , null=True)
    product_stock = models.IntegerField(default=0)
    product_uploadDate =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
