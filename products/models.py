from django.db import models

# Create your models here.
class Product(models.Model):

    name=models.CharField(max_length=200)
    weight=models.FloatField()
    price=models.FloatField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

    def __str__(self):
        return self.name
