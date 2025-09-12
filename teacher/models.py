from django.db import models

# Create your models here.
class teacher(models.Model):

    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    
    def __str__(self):  
        return self.name