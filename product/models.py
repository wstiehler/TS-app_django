from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated =  models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name

