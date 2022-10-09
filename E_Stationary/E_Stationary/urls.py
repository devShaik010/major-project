from django.contrib import admin
from django.urls import path , include
from Ink_Spot import urls

urlpatterns = [
    path('',include('Ink_Spot.urls')),
    path('admin/', admin.site.urls),
]
