from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Review(models.Model):
  product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  review = models.TextField()
  rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
  date_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return str(self.product) + ' >> ' + str(self.user)
  
