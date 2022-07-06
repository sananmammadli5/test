from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=55)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('indexpage')