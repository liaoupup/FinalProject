# Generated by Django 3.2.9 on 2021-11-28 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211128_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='motto',
            name='content',
            field=models.TextField(),
        ),
    ]
