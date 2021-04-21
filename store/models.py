from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='store/images/')
    description = models.TextField()
    ingredients = models.TextField(default='SOME STRING')

    def __str__(self):
        return self.name
