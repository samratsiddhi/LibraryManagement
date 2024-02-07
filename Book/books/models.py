from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
class Books(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    
    def __str__(self) -> str:
        return self.name
    
    