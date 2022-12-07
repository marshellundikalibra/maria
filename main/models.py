from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=55)
    price=models.FloatField()
    description=models.CharField(max_length=100)
    quantity=models.IntegerField()