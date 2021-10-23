from django import forms

from .models import News
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor_uploader.fields import RichTextUploadingField

class article_form(ModelForm):
    # body = forms.RichTextUploadingField(widget=forms.Textarea(attrs={"class":"form-control","cols":"10"}))
    class Meta:
        model = News
        fields = '__all__'
        exclude = ('writer',)