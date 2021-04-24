from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 100)

class Posts(models.Model):
    title = models.CharField(max_length=30)
    username = models.ForeignKey(User, on_delete=models.CASCADE)



