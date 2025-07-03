
from django.urls import path
from .import views

urlpatterns = [

   path('' , views.home , name = "Home"),
   path('aboutUs/' , views.aboutUs , name = "AboutUs"),
   path('productView/' , views.prod_view , name = "ViewProduct"),
   path('search/', views.search, name='Search'),
   path('checkout/' , views.checkout , name = "Checkout"),
   path('cart/' , views.cart , name = "Cart"),
   path('orders/' , views.orders , name = "Orders"),
]