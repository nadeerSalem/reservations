from django.db import models

# Create your models here.
class Reservation(models.Model):

    date = models.DateField(blank=True)
    cena = models.BooleanField(default=False)
    pranzo = models.BooleanField(default=True)
    adults = models.CharField(max_length=20, default=0)
    children = models.CharField(max_length=20, default=0)
    total_clients = models.CharField(max_length=20, default=0)
    name = models.CharField(max_length=50)
    email = models.EmailField() 
    phone_number = models.CharField(max_length=20)
    note = models.TextField(blank=True, default="")


