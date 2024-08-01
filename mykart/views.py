# from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from django.http import HttpResponse


def home(request):
    products = Product.objects.all().filter(is_available=True)
    # Product model is from store app models
    context = {
        'products':products,
    }

    return render(request,'home.html',context)