from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_birth=models.DateField()
    password=models.CharField(max_length=255)
    def __str__(self):
        return self.username