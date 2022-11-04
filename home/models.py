from unicodedata import category
from django.db import models
from pyexpat import model
from django.db import models
# Create your models here.
class categories(models.Model):
    category_name=models.CharField(max_length=50)
    category_icon=models.ImageField(upload_to='images/', null=True, blank=True)
    
