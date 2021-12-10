from django.db import models

# Create your models here.

class Persona(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_street = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.IntegerField()
    email =  models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    picture = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.first_name,self.first_name