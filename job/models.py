from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile= models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)

    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    def __str__(self) :
        return self.user.username
