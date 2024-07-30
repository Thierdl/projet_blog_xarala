from django.db import models


class Article(models.Model):
  title = models.CharField(max_length=150)
  summary = models.TextField(max_length=500) 
  content = models.TextField()
  author = models.CharField(max_length=100)
  date_create = models.DateTimeField(auto_now_add=True)
  date_updat = models.DateField(auto_now=True) 

  def __str__(self):
    return f"{self.title} {self.auteur}"

