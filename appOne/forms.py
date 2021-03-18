from django import forms
from .models import Content, Images

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=245)
    website = forms.URLField(max_length=245)
    github = forms.URLField(max_length=245)
 
    class Meta:
        model = Content
        fields = ('title', 'content', 'website', 'github')
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )