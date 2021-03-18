from django.db import models
from django.template.defaultfilters import slugify

def get_image_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)
class Content(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    website = models.URLField()
    github = models.URLField()
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
    
    
    def __str__(self):
        return self.title
    
    

