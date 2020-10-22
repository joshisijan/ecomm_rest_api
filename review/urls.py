from django.urls import path
from .views import *

urlpatterns = [
    path('add/', review_add, name="review_add"),
    path('<int:product_id>/<int:page_number>/<int:limit>/', review_home, name="review_home"),
    path('<int:product_id>/<int:page_number>/', review_home, name="review_home"),
    path('<int:product_id>/', review_home, name="review_home"),
]
