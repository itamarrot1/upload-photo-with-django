from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    comapny= models.CharField(max_length=20)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return self.name