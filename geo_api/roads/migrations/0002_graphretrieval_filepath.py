# Generated by Django 2.2.3 on 2019-07-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphretrieval',
            name='filepath',
            field=models.CharField(default='/', max_length=255),
            preserve_default=False,
        ),
    ]
