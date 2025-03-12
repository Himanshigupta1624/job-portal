from django.db import models
from users.models import CustomUser
from comapny.models import Comapny


class State(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Industry(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name    


class Job(models.Model):
    job_type_choices=(
        ('Remote','Remote'),
        ('Onsite','Onsite'),
        ('Hybrid','Hybrid')
    )
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    company=models.ForeignKey(Comapny,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    requirements=models.TextField()
    ideal_candidate=models.TextField()
    is_available=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    industry=models.ForeignKey(Industry,on_delete=models.DO_NOTHING,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.DO_NOTHING,null=True,blank=True)
    job_type=models.CharField(max_length=20,choices=job_type_choices,null=True,blank=True)
    
    
    def __str__(self):
        return self.title
    
class ApplyJob(models.Model):
    status_choices=(
        ('Accepted','Accepted'),
        ('Declined','Declined'),
        ('Pending','Pending')
        )
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=status_choices)   
