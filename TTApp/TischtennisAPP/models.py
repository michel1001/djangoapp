from django.db import models
from django.db.models.deletion import CASCADE

class TTUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    ttrpunkte = models.IntegerField(default=1000)
    verein = models.CharField(max_length=100, default='nicht angegeben')
    spielstil = models.CharField(max_length=30, default='shakehand')
    alter = models.IntegerField
class Trainingsplan(models.Model):
    ttuser = models.OneToOneField(TTUser, on_delete=models.CASCADE)
        

class Übungen(models.Model):
    name = models.CharField(max_length=50)
    komplexität = models.CharField(max_length=50)
    intensität = models.CharField(max_length=50)
    trainingsplan = models.ForeignKey(Trainingsplan, on_delete=models.CASCADE) 
