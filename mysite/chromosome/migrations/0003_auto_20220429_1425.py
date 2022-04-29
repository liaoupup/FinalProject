# Generated by Django 3.2.9 on 2022-04-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromosome', '0002_abnormal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abnormal',
            name='abnormal_type',
        ),
        migrations.AddField(
            model_name='abnormal',
            name='abnormal_type',
            field=models.ManyToManyField(related_name='abnormal', to='chromosome.AbnormalType'),
        ),
        migrations.AlterField(
            model_name='abnormal',
            name='image',
            field=models.ImageField(blank=True, help_text='建议核型图片数量在10张以内，支持 jpg/jpeg、png、bmp、tif 等图片格式', null=True, upload_to='images/'),
        ),
    ]