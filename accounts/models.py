from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class author(models.Model):
    state = [
    ('active','Active'),
    ('deactive','Deactive'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True,null=True)
    email = models.CharField(max_length=80,blank=True,null=True)
    status = models.CharField(max_length=20,blank=True,null=True,choices=state)

    def __str__(self):
        return self.name

