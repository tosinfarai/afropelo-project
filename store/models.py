from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = CloudinaryField('image')
    description = models.TextField()
    ingredients = models.TextField(default='')
    # created = models.DateTimeField()

    def __str__(self):
        return self.name
