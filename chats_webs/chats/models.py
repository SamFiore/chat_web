from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    
class Message(models.Model):
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now(tz=None),blank=True)
    room = models.CharField(max_length=1000)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'Sala: {self.room} | Autor: {self.author} | Fecha: {self.date.strftime("%d-%m-%y %H:%M:%S")}'
