from django.db import models

# Create your models here.

"""
1. Companiya nomi 
2. Descriptions
3. 
"""

class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, null=True)
    image = models.ImageField(upload_to='media/')
    working = models.PositiveIntegerField(default=0, null=True)
    level = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_info(self):
        return (f'{self.first_name}'
                f'{self.last_name}')

    def __str__(self):
        return self.get_info()


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='media/')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
