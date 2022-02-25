from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('navbase/', views.navbase, name='navbase'),
    path('display-body/', views.displaybody, name='display-body'),
    path('shop/', views.shop, name='shop'),
    path('why/', views.why, name='why'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
]