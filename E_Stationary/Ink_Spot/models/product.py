from django.db import models
from .categories import Categories

# this is for product card items 
class Product(models.Model):
    name = models.CharField(max_length=20)
    discount = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=40)
    image = models.ImageField(upload_to="Uploads\product")
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE, default=1)
