from django.shortcuts import render
from django.http import JsonResponse
from .models import Category

def categories_home(request): 
  categories = Category.objects.all().values()
  category_count = categories.count()
  response = {
      'count': category_count,
      'categories': list(categories),
    }
  return JsonResponse(response)
