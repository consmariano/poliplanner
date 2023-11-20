# Generated by Django 4.2.7 on 2023-11-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theportfolio', '0018_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='posts', to='theportfolio.category'),
        ),
    ]