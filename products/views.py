from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, ProductImage
from categories.models import Category
from django.core.paginator import Paginator

def products_home(request, page_number = 1, limit = 20): 
  # get total product count
  product_count = Product.objects.all().count()
  #calculate total pages
  total_pages = product_count / limit if limit < product_count else 1
  if total_pages != int(total_pages):
    total_pages = int(total_pages) + 1
  else:
    total_pages = int(total_pages)
  #calculate offset
  offset = (page_number - 1) * limit
  #get products based on page number
  products = Product.objects.all()[offset:limit + offset].values()
  #loop on all products to get category name and product images
  for product in products:
    productImages = ProductImage.objects.all().filter(product_id = product['id']).values()
    product['category_name'] = Category.objects.get(id = product['category_id']).name
    product['images'] = list(productImages)
  # make response dict
  response = {
      'count': product_count,
      'limit': limit,
      'total_pages': total_pages,
      'page': page_number,
      'products': list(products),
    }
  return JsonResponse(response)
