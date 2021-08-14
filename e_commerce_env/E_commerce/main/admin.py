from django.contrib import admin
from .models import Category, Brand, Color, Size, Product, ProductAttribute, Banner
# Register your models here.
admin.site.register(Banner)
admin.site.register(Size)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'color', 'size', 'price', 'status')
    list_editable = ['title', 'brand', 'color', 'size', 'price', 'status']


admin.site.register(Product, ProductAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'colorcode')


admin.site.register(Color, ColorAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'price')


admin.site.register(ProductAttribute, ProductAttributeAdmin)
