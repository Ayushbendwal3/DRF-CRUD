from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name
