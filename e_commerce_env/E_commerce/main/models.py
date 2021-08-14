from django.db import models


#Banner
class Banner(models.Model):
    img = models.CharField( max_length=200)
    alt_text = models.CharField(max_length=300)



# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/category_imgs/')

    def __str__(self):
        return self.title
#Brand
class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/brand_imgs/')

    def __str__(self):
        return self.title
#Color
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title
#Size
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title    = models.CharField(max_length=200)
    image    = models.ImageField(upload_to='upload/product_imgs/', height_field=None, width_field=None, max_length=None)
    slug     = models.CharField(max_length=50)
    detail   = models.TextField()
    specs    = models.TextField()
    price    = models.PositiveIntegerField()
    brand    = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    size     = models.ForeignKey(Size,on_delete=models.CASCADE)
    color    = models.ForeignKey(Color,on_delete=models.CASCADE)
    status   = models.BooleanField(default=True)


#Product Attribute
class ProductAttribute(models.Model):
    product  = models.ForeignKey(Product,on_delete=models.CASCADE)
    size     = models.ForeignKey(Size,on_delete=models.CASCADE)
    color    = models.ForeignKey(Color,on_delete=models.CASCADE)
    price    = models.PositiveIntegerField()

    def __str__(self):
        return self.product.title
