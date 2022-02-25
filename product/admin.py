from django.contrib import admin
from . models import SweetCategory, SweetBrand, SweetColor, SweetQuantity, SweetProduct, SweetBanner, SweetAttribute

# Register your models here.
admin.site.register(SweetBrand)
admin.site.register(SweetQuantity)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'image_tag')
admin.site.register(SweetCategory, CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'color_bg')
admin.site.register(SweetColor, ColorAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display  = ('alt_text', 'image_tag')
admin.site.register(SweetBanner, BannerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'brand', 'color', 'quantity', 'status')
    list_editable = ('status',)
admin.site.register(SweetProduct, ProductAdmin)

class SweetAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'quantity')
admin.site.register(SweetAttribute, SweetAttributeAdmin)
