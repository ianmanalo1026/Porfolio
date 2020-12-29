from django.db import models

class Content(models.Model):
    subject = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/')
    website = models.URLField()
    github = models.URLField()
    
    
    def __str__(self):
        return self.subject