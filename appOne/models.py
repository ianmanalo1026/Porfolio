from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Technology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.name)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    introduction = RichTextField(blank=True, null=True)
    website = models.URLField()
    github = models.URLField()
    
    def __str__(self):
        return str(self.user)
    

def get_image_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Content(models.Model):
    title = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    website = models.URLField()
    github = models.URLField()
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
    
    
    def __str__(self):
        return self.title
    
    

