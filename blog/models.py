from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
  title = models.CharField(max_length=100)
  summary = models.TextField(max_length=500) 
  content = models.TextField()

  #author = models.CharField(max_length=100)

  #A REVOIRE LIGNE 13
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  date_create = models.DateTimeField(auto_now_add=True)
  date_updat = models.DateTimeField(auto_now=True) 
  image = models.ImageField(null=True, upload_to="image_blog")

  def __str__(self):
    return f"{self.title} {self.author} {self.date_create}"
