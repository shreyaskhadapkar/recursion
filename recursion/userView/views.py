from django.shortcuts import render,redirect
from .models import Product
from django.urls import reverse

def homepage(request):
    return render(request,'userView/Homepage.html')

def scanner(request):
    return render(request,'userView/qrcode.html')

def cart(request):
    return render(request,'userView/cart.html')