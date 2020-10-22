from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(default="", blank=True)
  image = models.ImageField(blank=True, upload_to="images/category/")

  def __str__(self):
      return str(self.name)
  