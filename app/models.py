from django.db import models

# - `vehiclename` – CharField
# - `brand` – CharField
# - `model` – CharField
# - `price` – IntegerField
# - `fueltype` – CharField
# - `image` – ImageField (Vehicle image)
# Create your models here.

class Vehicle(models.Model):
    vehicle_name=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    price=models.IntegerField()
    fueltype=models.CharField(max_length=30)
    image=models.ImageField(upload_to="vehicle",null=True,blank=True)

