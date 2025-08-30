from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from django.http import JsonResponse
from .serializers.product import product_serializer


def index(request):
    return HttpResponse("<h4>Test process</h4>")


def about(request):
    return HttpResponse("<h4>page about us </h4>")


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>articles by categories</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Archive for years</h1><p>{year}</p>")


def get_all_products(request):
    products = Product.objects.all()
    data = [product_serializer(product) for product in products]
    return JsonResponse(data, safe=False)