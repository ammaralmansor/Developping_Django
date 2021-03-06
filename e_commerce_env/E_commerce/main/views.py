from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Category, Brand, Product, ProductAttribute, Banner
from django.template.loader import render_to_string
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
    related_products = Product.objects.filter(category = data.category ).exclude(id=id)[:4]
    return render(request, 'product_detail.html', {'data': data,'related':related_products})

def search(request):
    q = request.GET['q']
    data = Product.objects.filter(title__icontains = q,).order_by('-id')
    return render(request, 'search.html', {'data': data})

def filter_data(request):
    colors=request.GET.getlist('color[]')
    categories=request.GET.getlist('category[]')
    brands=request.GET.getlist('brand[]')
    sizes=request.GET.getlist('size[]')
    allProducts=Product.objects.all().order_by('-id').distinct()
    if len(colors)>0:
        allProducts=allProducts.filter(productattribute__color__id__in=colors).distinct()
    if len(categories)>0:
        allProducts=allProducts.filter(category__id__in=categories).distinct()
    if len(brands)>0:
        allProducts=allProducts.filter(brand__id__in=brands).distinct()
    if len(sizes)>0:
        allProducts=allProducts.filter(productattribute__size__id__in=sizes).distinct()
    t=render_to_string('ajax/product-list.html',{'data':allProducts})
    return JsonResponse({'data':t})


def card(request):
    return render(request , 'card.html')


def loggin(request):
    return render(request , 'loggin.html')


def singnup(request):
    return render(request , 'singnup.html')

def password_reset(request):
    return render(request , 'password_reset.html')

def team(request):
    return render(request , 'team.html')
