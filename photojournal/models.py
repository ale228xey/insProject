from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photojournal/static/images')
    description = models.TextField(max_length=100)
    creation = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    creation = models.DateTimeField(auto_now=True)