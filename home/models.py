from django.db import models
from django import forms
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Mypost(models.Model):
    STATUS_CHOICES = (

        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_posts')
    image = models.ImageField(upload_to='image/%Y/%m/%d',
                              blank=True)
    detail=RichTextUploadingField()
    files = models.FileField(upload_to='file/%Y/%m/%d', blank=True)
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="draft")


