from django.contrib import admin
from .models import Category,Brand,Color,Size,Product , ProductAttribute
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand','color','size','price','status')
    list_editable = ['title','brand','color','size','price','status']


admin.site.register(Product,ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','product','color','size','price')

    
admin.site.register(ProductAttribute,ProductAttributeAdmin)


