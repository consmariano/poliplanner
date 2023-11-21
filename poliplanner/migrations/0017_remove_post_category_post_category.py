# Generated by Django 4.2.7 on 2023-11-20 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poliplanner', '0016_remove_post_category_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]