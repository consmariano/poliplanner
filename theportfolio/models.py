from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

