from django.db import models


# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    Timg = models.ImageField(upload_to='pics')
    Tname = models.CharField(max_length=250)
    Tdesc = models.TextField()

    def __str__(self):
        return self.Tname

class Argent(models.Model):
    nam=models.CharField(max_length=150)
    im=models.ImageField(upload_to='argpic')
    des=models.TextField()

    def __str__(self):
        return self.nam