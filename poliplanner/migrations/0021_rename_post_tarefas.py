# Generated by Django 4.2.7 on 2023-11-23 02:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poliplanner', '0020_rename_category_subject_rename_category_post_subject'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Tarefas',
        ),
    ]
