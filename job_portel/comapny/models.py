from django.db import models
from users.models import CustomUser

class Comapny(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='company')
    name=models.CharField(max_length=100,null=True,blank=True)
    est_date=models.PositiveIntegerField(null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
    