# Generated by Django 3.2.9 on 2021-11-27 17:15

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_motto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='motto',
            name='content',
            field=martor.models.MartorField(),
        ),
    ]