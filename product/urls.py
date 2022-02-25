from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import DetailProductList, DetailBrandList

urlpatterns = [
    path('category-list/', views.category_list, name = 'category-list'),
    path('brand-list/', views.brand_list, name = 'brand'),
    path('product-list/', views.product_list, name = 'productlist'),
    path('detail-product-list/<int:id>/', DetailProductList.as_view(), name = 'detailproductlist'),
    path('detail-brand-list/<int:id>/', DetailBrandList.as_view(), name = 'detailbrandlist'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
