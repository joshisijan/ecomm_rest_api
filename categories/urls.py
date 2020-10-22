from django.urls import path
from .views import *

urlpatterns = [
    path('', categories_home, name="categories_home"),
]
