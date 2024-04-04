from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    news_image = CloudinaryField('image',blank=True)
    short_description = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    video_url = models.FileField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)