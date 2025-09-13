from django.db import models

# Create your models here.

class Parents(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    
    def __str__(self):  
        return self.name