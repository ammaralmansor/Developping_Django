from django.urls import path,include
from .views import index,category_list,brand_list,product_list ,category_product_list ,brand_product_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('category_list',category_list,name='category_list'),
    path('brand_list',brand_list,name='brands'),
    path('product_list',product_list,name='product_list'),
    path('category_product_list/<int:cat_id>',category_product_list,name='category_product_list'),
    path('brand_product_list/<int:brand_id>',brand_product_list,name='brand_product_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)