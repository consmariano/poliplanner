# Generated by Django 4.2.7 on 2023-11-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poliplanner', '0006_alter_comment_options_rename_date_comment_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='post_comments', to='poliplanner.comment'),
        ),
    ]
