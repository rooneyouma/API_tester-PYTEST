from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    
