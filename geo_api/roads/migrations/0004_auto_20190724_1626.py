# Generated by Django 2.2.3 on 2019-07-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0003_auto_20190724_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphretrieval',
            name='filepath',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
