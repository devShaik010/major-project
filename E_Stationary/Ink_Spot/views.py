from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

# Create your views here.



def index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'signup.html')


product = Product.get_all()
data = {} 
data['product'] = product


def cat(request):
    return render(request, 'product.html',data)