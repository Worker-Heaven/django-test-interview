from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=60)
    contact_name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
