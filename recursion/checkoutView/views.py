from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order
from userView.models import CartItem,Cart
from logisticsView.models import Product
from django.contrib.auth.models import User
from django.urls import reverse

# @login_required
def orderList(request):
    if request.user.username == 'srajan':
        if request.method == 'POST':
            cart_id = request.POST.get('cart_id')
            return redirect(reverse('orderDetails',kwargs={'slug':cart_id}))

        print('Printed in orderList')
        params = dict()
        orders = Order.objects.all()

        listData = []
        for i in orders:
            data = {}
            name = Cart.objects.get(cart_id = i.cart_id.cart_id)
            data['order_id'] = i.order_id
            data['cart_id'] = i.cart_id.cart_id
            data['user_name'] = name.user_id
            listData.append(data)

        params = {'data':listData}
        print(listData)
        return render(request,'checkoutView/orderlist.html',params) 
    else:
        return HttpResponse("You dont belong here")

def orderDetails(request,slug):
    cart = CartItem.objects.filter(cart_id=slug)
    params = dict()
    listData = []
    sumTotal = 0
    for i in cart:
        data = {}
        id = i.product_id.product_id
        productName = i.product_id.product_name
        quantity = i.item_quantity
        productObject = Product.objects.get(product_id=id)
        rate = productObject.rate
        totalRate = quantity * rate 
        print(id,productName,quantity,rate ,totalRate)
        data['id']=id
        data['productName']=productName
        data['quantity']=quantity
        data['rate']=rate
        data['totalRate']=totalRate
        sumTotal += totalRate
        listData.append(data)
    params = {'data':listData,'sumTotal':sumTotal,'id':id}
    print(sumTotal)
    return render(request,'checkoutView/orderDetails.html',params)