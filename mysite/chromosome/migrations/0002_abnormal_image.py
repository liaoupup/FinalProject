# Generated by Django 3.2.9 on 2022-04-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromosome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abnormal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
