from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True,unique=True,null=False,blank=False)
    product_name = models.CharField(max_length=100)
    available_quantity = models.IntegerField()
    rate = models.IntegerField()
    
    def __str__(self):
        return self.product_name
