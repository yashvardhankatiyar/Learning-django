from django.db import models

class Destination(models.Model):
    
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(default='no description available')
    price = models.IntegerField(default=0)
    isOffer = models.BooleanField(default=False)

  