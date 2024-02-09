from django.db import models

# Create your models here.
class Booklog(models.Model):
    book_id = models.JSONField()
    user_id = models.IntegerField()