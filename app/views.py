from django.shortcuts import render,HttpResponse
from .models import Product
# Create your views here
def product_list(request,category_slug=None):
    # product_list = Product.objects.filter(available=True)
    return render(request,'base.html')
    # return HttpResponse("Hello")