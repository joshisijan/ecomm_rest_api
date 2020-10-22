from django.urls import path
from .views import *

urlpatterns = [
    path('<int:page_number>/<int:limit>', products_home, name="products_home"),
    path('<int:page_number>/', products_home, name="products_home"),
    path('', products_home, name="products_home"),
]
