from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=15, blank=True)
   
    password   = models.CharField(max_length=100)
