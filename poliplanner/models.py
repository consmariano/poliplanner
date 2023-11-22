from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.hashers import make_password

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    USER_TYPE = ((1, "Gerente"), (2, "Professor"), (3, "Aluno"))
    
    nusp = models.CharField(max_length=20, unique=True)  # Adicionado campo NUSP
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    #profile_pic = models.ImageField()
    fcm_token = models.TextField(default="")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "nusp"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.last_name + ", " + self.first_name

CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_set'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_set'

class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

#######################################################################

class Curso(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Gerente(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True, blank=False)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.last_name + " " + self.admin.first_name

class Professor(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.last_name + " " + self.admin.first_name

class Oferecimento(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        start_date_formatted = self.start_year.strftime('%d/%m/%Y')
        end_date_formatted = self.end_year.strftime('%d/%m/%Y')
        return f"From {start_date_formatted} to {end_date_formatted}"

class Subject(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default='Objetivos da disicplina.')
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,)
    oferecimento = models.ForeignKey(Oferecimento, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name

class Aluno(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True, blank=False)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.admin.last_name + ", " + self.admin.first_name

class Tarefa(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Professor, on_delete=models.CASCADE)
    content = models.TextField(default='Descrição da atividade.')
    deadline = models.DateTimeField(blank=False)
    subject = models.ManyToManyField(Subject, related_name="tarefas", blank=False)

    def __str__(self):
        return self.title + ' | ' + str(self.deadline) + ' | ' + str(self.subject)
    
    def get_absolute_url(self):
        return reverse('post_single', args=(str(self.id)) )

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_comments", on_delete=models.CASCADE, default=1)
    username = models.CharField(max_length=255)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    tarefa = models.ForeignKey(Tarefa, related_name='post_comments', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '%s - %s' % (self.tarefa.title, self.username)

    class Meta:
        ordering = ['-post_date']
    
@receiver(post_save, sender=Comment)
def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        # Adiciona o comentário automaticamente à postagem relacionada
        instance.post.post_comments.add(instance)
