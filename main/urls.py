from django.urls import path, re_path, register_converter
from .  import views
from . import converters
from .views import get_all_products

register_converter(converters.FourDigitYearConverter,"year4")
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path("archive/<year4:year>/", views.archive),
    path('products/', get_all_products, name='product-list'),
]
