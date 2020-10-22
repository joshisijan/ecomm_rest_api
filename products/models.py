from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=200)
  category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
  description = models.TextField()
  price = models.FloatField()
  discount = models.FloatField(default = 0.0, blank=True)

  def __str__(self):
      return str(self.name)
  

class ProductImage(models.Model):
  product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
  image = models.FileField(upload_to = 'images/product/')

  def __str__(self):
      return str(self.image.name)
  
  
