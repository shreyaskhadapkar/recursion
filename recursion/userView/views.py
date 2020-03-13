from django.shortcuts import render,redirect
from .models import Product
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from logisticsView.models import Product
from .models import Cart,CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def homepage(request):
    return render(request,'userView/Homepage.html')

@login_required
@csrf_exempt
def scanner(request):
    global flag
    if request.method=='GET' :
        if Cart.objects.filter(user_id=request.user):
            pass
        else:
            cart = Cart.objects.create(user_id=request.user)
        
    if request.method == 'POST':
        product = Product.objects.get(product_id = request.POST['key'])
        cart = Cart.objects.get(user_id=request.user)
        item_quantity = 1
        cart_item = CartItem.objects.create(product_id=product,cart_id=cart,item_quantity=item_quantity)

    return render(request,'userView/qrcode.html')

@login_required
def cart(request):
    user = request.user
    cart = Cart.objects.get(user_id=user)
    cart_item = CartItem.objects.filter(cart_id=cart.cart_id)
    listData = []
    sum = 0
    for i in cart_item:
        data = {}
        data['product_name'] = i.product_id.product_name
        data['rate'] = i.product_id.rate
        data['item_quantity'] = i.item_quantity
        data['cost'] = data['rate']*data['item_quantity']
        listData.append(data)

        sum = sum + data['cost']

    params = { 'data':listData, 'Total':sum }
    return render(request,'userView/cart.html',params)