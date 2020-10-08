from django.db import models

# Create your models here.
class User(models.Model):

    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    uploads = models.FileField(upload_to='uploads/')