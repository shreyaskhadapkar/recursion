from django.db import models
from userView.models import Cart

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True,unique=True,null=False,blank=False)
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE)

    def __str__(self):
        return self.str(order_id)