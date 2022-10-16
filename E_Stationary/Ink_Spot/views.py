from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.categories import Categories

# Create your views here.



def index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'signup.html')

cat = Categories.all_catogaries()

product = Product.get_all()
data = {} 
data['product'] = product
data['catogereis'] = cat

def cat(request):
    return render(request, 'product.html',data)

def book(request):
    return render(request, 'books.html')    