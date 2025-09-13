from django.db import models

# Create your models here.
class Stuff(models.Model):

    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    
    def __str__(self):  
        return self.name