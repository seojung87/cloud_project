from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

class Cash(models.Model):
    amount = models.IntegerField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    memo = models.TextField()




