from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"


class Pharmacies(models.Model):
    name = models.CharField(max_length=80)
    place = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} - {self.place} - {self.phone_number}"


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name} - {self.email}"
