# Generated by Django 4.2.7 on 2023-11-23 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poliplanner', '0019_alter_category_name_remove_post_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Subject',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='subject',
        ),
    ]