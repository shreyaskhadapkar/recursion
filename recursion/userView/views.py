from django.shortcuts import render,redirect
from .models import Product
from django.urls import reverse

# Create your views here.

def homepage(request):
    return render(request,'userView/Homepage.html')
