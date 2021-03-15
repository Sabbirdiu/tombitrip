from django.db import models
from datetime import datetime
from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Traveller(models.Model):
    overview = RichTextUploadingField()
    def __str__(self):
         return self.overview

class Faq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,blank=True)
    overview = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name        