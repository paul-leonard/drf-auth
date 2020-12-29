from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Entry(models.Model):
  title = models.CharField(max_length=64)
  story = models.TextField(default="Guess it wasn't that interesting")
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.title + " by " + self.author