# Generated by Django 3.2.9 on 2022-04-30 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chromosome', '0004_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='abnormal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='chromosome.abnormal'),
        ),
    ]