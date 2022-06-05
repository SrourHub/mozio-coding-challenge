from django.db import models

# Create your models here.

class Provider(models.Model):

    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    language = models.CharField(max_length=25)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ServiceArea(models.Model):

    name = models.CharField(max_length = 50)
    price = models.FloatField()
    geojson_information = models.CharField(max_length=200)

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

