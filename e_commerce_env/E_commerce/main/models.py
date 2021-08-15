from django.db import models
from django.utils.html import mark_safe

# Banner


class Banner(models.Model):
    img = models.ImageField(upload_to='upload/banners_imgs/')
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = '1.Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" /' % (self.img.url))

    def __str__(self):
        return self.alt_text


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/category_imgs/')

    class Meta:
        verbose_name_plural = '2.Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
# Brand


class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/brand_imgs/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    class Meta:
        verbose_name_plural = '3.Brands'

    def __str__(self):
        return self.title
# Color


class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '4.Colors'

    def colorcode(self):
        return mark_safe('<div style="width:40px; height:20px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title
# Size


class Size(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '5.Sizes'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload/product_imgs/',
                              height_field=None, width_field=None, max_length=None)
    slug = models.CharField(max_length=50)
    detail = models.TextField()
    specs = models.TextField()
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default = False)

    class Meta:
        verbose_name_plural = '6.Products'


# Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = '7.ProductAttributes'

    def __str__(self):
        return self.product.title
