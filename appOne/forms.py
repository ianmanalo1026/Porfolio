from django import forms
from django.db.models import fields
from ckeditor.widgets import CKEditorWidget
from .models import Content



class ContentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Content
        fields = '__all__'