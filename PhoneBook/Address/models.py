from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    address = models.TextField(max_length=300)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
