from django.db import models
# from django.db.models.deletion import PROTECT
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.postgres.fields import ArrayField

from accounts.models import author

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=500,blank=True,null=True)
    short_desc = models.TextField(max_length=500,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    main_image = models.ImageField(upload_to = "news",blank = True,null = True)
    main_image_url = models.CharField(max_length=1000,blank=True,null=True)
    writer = models.ForeignKey(author,on_delete=models.PROTECT)
    body = RichTextUploadingField(blank= True,null = True)
    meta_title = models.CharField(max_length=700,blank=True,null=True)
    meta_keyword = models.CharField(max_length=700,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    # tags = ArrayField(models.CharField(max_length=200), blank=True,size=8,null=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    belong_to = models.ForeignKey(News,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True,null=True)
    body = models.TextField(max_length=5000,blank=True,null=True)
    emal = models.CharField(max_length=100,blank=True,null=True)

class Trend(models.Model):
    new = models.ForeignKey(News,on_delete=models.SET_NULL,blank=True,null=True)

    # def __str__(self):
    #     return self.new

class Banner(models.Model):
    new = models.ForeignKey(News,on_delete=models.CASCADE,blank=True,null=True)
