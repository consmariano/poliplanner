# Generated by Django 4.2.7 on 2023-11-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poliplanner', '0010_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content',
            field=models.TextField(default='Default Content'),
        ),
    ]