from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.template import context

from goods.forms import ProductForm
from goods.models import Products
from goods.utils import q_search

def catalog(request, category_slug=None):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    rooms = request.GET.get('rooms', None)
    max_area = request.GET.get('max_area', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    
    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        
    if on_sale:
        goods = goods.filter(booked_booking=False)
    
    if rooms:
        goods = goods.filter(rooms=rooms)
        
    if max_area:
        goods = goods.filter(discount__lte=max_area)
        
    if min_price:
        goods = goods.filter(price__gte=min_price)

    if max_price:
        goods = goods.filter(price__lte=max_price)
        
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)
        
    context = {
        'title': 'Home - Каталог',
        'goods': goods,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    
    context = {
        'title': 'Home - Оголошення',
        'product': product
    }
        
    return render(request, 'goods/product.html', context=context)
