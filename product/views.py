from django.shortcuts import render
from . models import SweetCategory, SweetBrand, SweetProduct
from django.views.generic.base import TemplateView, View

# Create your views here.
def category_list(request):
    data = SweetCategory.objects.all().order_by('-id')
    return render(request, 'product/category.html', {'data' : data})


def brand_list(request):
    brands = SweetBrand.objects.all().order_by('-id')
    return render(request, 'product/brand.html', {'brands' : brands})


def product_list(request):
    products = SweetProduct.objects.all().order_by('-id')
    return render(request, 'product/productlist.html',
     {'products' : products})


class DetailProductList(View):
    template_name = 'product/detailproductlist.html'
    def get(self, request, id):
       cat = SweetCategory.objects.get(id = id)
       product = SweetProduct.objects.filter(category = cat)
       return render(request, self.template_name, {'product' : product})


class DetailBrandList(View):
    template_name = 'product/detailbrand.html'
    def get(self, request, id):
        get_brand = SweetBrand.objects.get(id = id)
        brands = SweetProduct.objects.filter(brand = get_brand)
        return render(request, self.template_name, {'brands' : brands})


