from django.db import models

# Create your models here.

class Tashkilot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
