from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Create your models here.
class SweetCategory(models.Model):
    category_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images')

    class Meta:
        verbose_name_plural = '4. SweetCategory'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.category_name


class SweetBrand(models.Model):
    brand_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images')

    class Meta:
        verbose_name_plural = '3. SweetBrand'

    def __str__(self):
        return self.brand_name

class SweetColor(models.Model):
    color_name = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = '5. SweetColor'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_name))
    
    def __str__(self):
        return self.color_name


class SweetQuantity(models.Model):
    quantity = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = '7. SweetQuantity'

    def __str__(self):
        return self.quantity


class SweetProduct(models.Model):
    product_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images')
    slug = models.CharField(max_length = 100)
    detail = models.TextField()
    price = models.PositiveIntegerField(null = True)
    category = models.ForeignKey(SweetCategory, on_delete = models.CASCADE)
    brand = models.ForeignKey(SweetBrand, on_delete = models.CASCADE)
    color = models.ForeignKey(SweetColor, on_delete = models.CASCADE)
    quantity = models.ForeignKey(SweetQuantity, on_delete = models.CASCADE)
    status = models.BooleanField(default = True)

    class Meta: 
        verbose_name_plural = '6. SweetProduct'

    def __str__(self):
        return self.product_name

    
class SweetBanner(models.Model):
    image = models.ImageField(upload_to = 'images')
    alt_text =models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = '2. SweetBanner'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text


class SweetAttribute(models.Model):
    product = models.ForeignKey(SweetProduct, on_delete = models.CASCADE)
    color = models.ForeignKey(SweetColor, on_delete = models.CASCADE)
    quantity = models.ForeignKey(SweetQuantity, on_delete = models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = '1. SweetAttribute'

    def __str__(self):
        return self.product.product_name

    def image_tag(self):
       return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    