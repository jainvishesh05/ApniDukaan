from asyncio.windows_events import NULL
from operator import truediv
from pickle import TRUE
from django.shortcuts import render
from .models import Product , Categories
import math



# Create your views here.
def chunk_products(products , size):
    for i in range(0 , len(products) ,size):
        yield products[i:i+size]

def home(request):
    product = Product.objects.all()
    category = Categories.objects.all()
    product_chunks = chunk_products(product , 4)
    category_chunks = chunk_products(category , 3)
    context = { 'product_chunks' : product_chunks , 
                'category_chunks': category_chunks,
                'all_categories': category,
                }
    return render(request , 'shop/home.html' , context)

def cart(request):
    return render(request , 'shop/cart.html' )

def aboutUs(request):
    return render(request , 'shop/aboutUs.html' )

def orders(request):
    return render(request , 'shop/orders.html' )

def prod_view(request):
    return render(request , 'shop/prod_view.html' )

def checkout(request):
    return render(request , 'shop/checkout.html' )

def search(request):
    return render(request , 'shop/search.html')

def wishlist(request):
    return render(request , 'shop/wishlist.html')
