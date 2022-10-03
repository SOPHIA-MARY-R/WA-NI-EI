from django.db import models
from django.forms import FileInput
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
     title = models.CharField(max_length=50)
     file = models.FileField()
     created_at = models.DateTimeField(auto_now_add=True)
     #file_of=models.ForeignKey(User, on_delete=models.CASCADE)
     def __str__(self): #function to name instances
        return self.title
