from django.db import models
from users.models import CustomUser


class REsume(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    job_title=models.CharField(max_length=100,null=True,blank=True)
    upload_resume=models.FileField(upload_to='resume',null=True,blank=True)
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"