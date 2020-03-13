from django.shortcuts import render,redirect
from .models import Product
from django.urls import reverse

def product(request):
    if request.method == 'POST':
        if 'update' in request.POST:
            id = request.POST.get('id')
            return redirect(reverse('productUpdate',kwargs={'slug':id}))
        elif 'delete' in request.POST:
            id = request.POST.get('id')
            Product.objects.get(product_id=id).delete()
        elif 'add' in request.POST:
            return redirect(reverse('productAdd'))
            

    product_queryset = Product.objects.all()
    params = { 'data' : product_queryset }
    return render(request,'logistics/product.html',params)

def productUpdate(request,slug):
    product = Product.objects.get(product_id=slug)
    params={'data':product}

    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.available_quantity = request.POST.get('available_quantity')
        product.rate = request.POST.get('rate')
        product.save()
        return redirect(reverse('product'))
    
    return render(request,'logistics/productUpdate.html',params)

def productAdd(request):

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        available_quantity = request.POST.get('available_quantity')
        rate = request.POST.get('rate')
        Product.objects.create(
            product_name=product_name,
            available_quantity=available_quantity,
            rate=rate
            )
        return redirect(reverse('product'))
    
    return render(request,'logistics/productAdd.html')
