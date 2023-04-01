from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class User(models.Model):
    """This is the base class for user model"""
    u_id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    text = models.TextField(max_length=255, default='Not Available')
    profile = models.ImageField(upload_to = 'images')
 
    def img_preview(self):
        """This function Display the image preview"""
        return mark_safe(f'<img src = "{self.profile.url}" width = "75" height="75" border-radius:"30" />')