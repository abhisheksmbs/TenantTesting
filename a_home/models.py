from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class SiteSettings(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default="#000000") 
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    

    def __str__(self):
        return self.name