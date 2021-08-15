from django.contrib import admin
from .models import Category, Brand, Color, Size, Product, ProductAttribute, Banner
# Register your models here.
admin.site.register(Size)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')


admin.site.register(Banner, BannerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')


admin.site.register(Product, ProductAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'colorcode')


admin.site.register(Color, ColorAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'price')


admin.site.register(ProductAttribute, ProductAttributeAdmin)
