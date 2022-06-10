from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from door_shop.models import Product




class ProductList(ListView):
    model = Product
    template_name = "index.html"









