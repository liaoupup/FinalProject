# Generated by Django 3.2.9 on 2021-11-28 07:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_motto_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='motto',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
