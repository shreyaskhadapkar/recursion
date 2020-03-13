from django.db import models
from django.contrib.auth.models import User
from logisticsView.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True,unique=True,null=False,blank=False)
    user_id = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cart_id)

class CartItem(models.Model):
    cartItem_id = models.IntegerField(primary_key=True,unique=True,null=False,blank=False)
    product_id = models.ForeignKey(Product, null=True, blank=True,on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, null=True, blank=True,on_delete=models.CASCADE)
    item_quantity = models.IntegerField()

    def __str__(self):
        return str(self.cartItem_id)


    

