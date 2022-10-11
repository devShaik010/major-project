from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('signup',sign_up),
    path('catogeries',cat)
]
