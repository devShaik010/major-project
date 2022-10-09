from django.contrib import admin
from .models.product import Product
from .models.categories import Categories

class product_display(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'categories']
    
class categories_display(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product, product_display)
admin.site.register(Categories,categories_display)
admin.site.site_header = "[ Admin ] Ink Spot"
