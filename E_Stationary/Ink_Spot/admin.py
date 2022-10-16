from django.contrib import admin
from .models.product import Product
from .models.categories import Categories
from .models.book import Book
from .models.b_catogeries import B_categories


# class Books(admin.ModelAdmin):
#     list_display = ['name', 'a_uth', 'desc', 'categories']
    
# class B_categories_display(admin.ModelAdmin):
#     list_display = ['name']

class product_display(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'categories']
    
class categories_display(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product, product_display)
admin.site.register(Categories,categories_display)
admin.site.register(Book)
admin.site.register(B_categories)
admin.site.site_header = "[ Admin ] Ink Spot"
