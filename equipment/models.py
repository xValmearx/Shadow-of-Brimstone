from django.db import models

# Create your models here.

class Token(models.Model):

    name = models.CharField(default= "Token")
    description = models.TextField(default= "Discard to ")
    
    def __str__(self):
        return self.name