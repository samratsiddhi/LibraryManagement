from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
class Books(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    created_at = models.TimeField(auto_now_add=True)
    quantity = models.IntegerField()
    

    
    