from django.db import models
from django.db.models.query_utils import subclasses

class Content(models.Model):
    subject = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/')
    github = models.URLField()
    
    
    def __str__(self):
        return self.subject
    
class about(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    training = models.TextField(max_length=1000)
    
    