# Generated by Django 3.2.9 on 2021-11-28 07:30

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211128_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motto',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
