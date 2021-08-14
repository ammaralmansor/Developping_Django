from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Brand, Product , ProductAttribute
# Create your views here.


def index(request):
    return render(request, 'index.html')

# categoies


def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'categories_list.html', context={'data': data})
# brand


def brand_list(request):
    data = Brand.objects.all().order_by('-id')
    return render(request, 'brand_list.html', context={'data': data})

# brand


def product_list(request):
    data = Product.objects.all().order_by('-id')
    cats = Product.objects.distinct().values('category__title', 'category__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    sizes = Product.objects.distinct().values('size__title', 'size__id')
    colors = Product.objects.distinct().values('color__title', 'color__id','color__color_code')
    return render(request, 'product_list.html', context={
        'data': data,
        'cats': cats,
        'brands': brands,
        'color':colors,
        'size':sizes,

    })
