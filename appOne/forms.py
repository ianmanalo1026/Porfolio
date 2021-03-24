from django import forms
from django.db.models import fields
from ckeditor.widgets import CKEditorWidget
from .models import Content



class ContentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    title = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    website = forms.URLField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    github = forms.URLField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Content
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()