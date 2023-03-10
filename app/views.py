from django.shortcuts import render, get_object_or_404
from .models import Product,Category


# Create your views here
def product_list(request, category_slug=None):
    category = None
    categorys = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html',{'category':category,
                                                'categorys':categorys,
                                                'products':products})
