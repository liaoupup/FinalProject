# Generated by Django 3.2.9 on 2021-11-22 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_last_created_time_blog_last_updated_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='type',
            new_name='blog_type',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
