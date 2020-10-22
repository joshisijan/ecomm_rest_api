from django.urls import path
from .views import *

urlpatterns = [
    path('', products_home, name="products_home"),
]
