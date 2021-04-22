from django.db import models
import mimetypes

# Create your models here.
class food_item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to ='FUDIEE/')
    price = models.IntegerField()
    type = models.CharField(max_length=20)

 