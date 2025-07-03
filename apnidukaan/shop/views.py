from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'shop/home.html')

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
