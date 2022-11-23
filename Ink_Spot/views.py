from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.categories import Categories
from .models.book import Book
from .models.b_catogeries import B_categories

# Create your views here.



def index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')


# for product _ stationary items

cat = Categories.all_catogaries()

product = Product.get_all()
data = {} 
data['product'] = product
data['catogereis'] = cat



# for Books

bcat = B_categories.all_catogaries()

book = Book.get_all()
bdata = {} 
bdata['book'] = book
bdata['b_catogereis'] = bcat

def cat(request):
    return render(request, 'product.html',data)

def book(request):
    return render(request, 'book.html',bdata)    