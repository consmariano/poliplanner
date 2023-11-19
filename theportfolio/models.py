from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('post_single', args=(str(self.id)) )

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_comments", on_delete=models.CASCADE, default=1)
    username = models.CharField(max_length=255)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.username)

    class Meta:
        ordering = ['-post_date']
    
@receiver(post_save, sender=Comment)
def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        # Adiciona o comentário automaticamente à postagem relacionada
        instance.post.post_comments.add(instance)
