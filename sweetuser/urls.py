from django.urls import path
from . import views
urlpatterns = [
    path('user-home/', views.user_home, name = 'userhome'),

]