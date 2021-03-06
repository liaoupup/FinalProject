# Generated by Django 3.2.9 on 2022-04-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromosome', '0003_auto_20220429_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(help_text='PubMed唯一标识码', verbose_name='PMID')),
                ('title', models.CharField(help_text='请输入标题', max_length=40, verbose_name='标题')),
                ('abstract', models.TextField(help_text='请输入摘要', verbose_name='摘要')),
                ('pdf', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
