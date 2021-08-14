from django.shortcuts import render
from django.http import HttpResponse
from .models import Category , Brand
# Create your views here.


def index(request):
    return render(request,'index.html')

#categoies
def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request,'categories.html',context={'data':data})
#brand
def brand_list(request):
    data = Brand.objects.all().order_by('-id')
    return render(request,'brand.html',context={'data':data})