from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Brand, Product, ProductAttribute, Banner
# Create your views here.


def index(request):
    banners = Banner.objects.all().order_by('-id')
    data = Product.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'index.html', {'data': data, 'banners': banners})

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
    #min_price = ProductAttribute.objects.aggregate(min('price'))
    #max_price = ProductAttribute.objects.aggregate(max('price'))

    return render(request, 'product_list.html', context={
        'data': data,
        # 'min_price':min_price,
        # 'max_price':max_price,
    })

# product list according to category


def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'category_product_list.html', context={
        'data': data,
    })

# product list according to brand


def brand_product_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    data = Product.objects.filter(brand=brand).order_by('-id')

    return render(request, 'category_product_list.html', context={
        'data': data,
    })

# Product Detail


def product_detail(request, slug, id):
    data = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'data': data})
