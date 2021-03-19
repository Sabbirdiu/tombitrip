from django.db import models
from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Experience(models.Model):
    title_keyword = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    overview = RichTextUploadingField()
    image = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/')
    title1 = models.CharField(max_length=100)
    overview1 = RichTextUploadingField()
    image1 = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title_keyword

    def get_absolute_url(self):
        return reverse('exp-details', kwargs={
            'slug': self.slug
        })    