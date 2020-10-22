from django.shortcuts import render
from django.http import JsonResponse
from .models import Review
from django.views.decorators.csrf import csrf_exempt
import html

# importing models
from products.models import Product
from django.contrib.auth.models import User

# getter for reviews
def review_home(request, product_id, page_number = 1, limit = 20): 
  # securing divisivle by 0
  if limit == 0:
    limit = 1
  # get total review count
  review_count = Review.objects.all().filter(product__id = product_id).count()
  #calculate total pages
  total_pages = review_count / limit if limit < review_count else 1
  if total_pages != int(total_pages):
    total_pages = int(total_pages) + 1
  else:
    total_pages = int(total_pages)
  #calculate offset
  offset = (page_number - 1) * limit

  reviews = Review.objects.all().filter(product__id = product_id)[offset:limit + offset].values()
 
  # make response dict
  response = {
      'count': review_count,
      'limit': limit,
      'total_pages': total_pages,
      'page': page_number,
      'product_id': product_id,
      'reviews': list(reviews),
    }
  return JsonResponse(response)

# setter for reviews
@csrf_exempt
def review_add(request):
  if request.method == 'POST':
    if request.POST.get('review') is not None and request.POST.get('user_id') is not None and request.POST.get('product_id') and request.POST.get('rating'):
      # review parameters to variable
      review = html.escape(request.POST.get('review').strip())
      user_id = request.POST.get('user_id')
      product_id = request.POST.get('product_id')
      rating = request.POST.get('rating')
      # making review instance
      review = Review()
      review['review'] = review
      review['product'] = Product.object.get(id = product_id)
      review['user'] = User.object.get(id = user_id)
      review['rating'] = rating
      review.save()
      return JsonResponse({'message': 'no error'})
  return JsonResponse({'message': 'argument error'})