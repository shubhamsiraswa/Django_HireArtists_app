# Generated by Django 3.2.3 on 2021-05-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_ref',
            field=models.URLField(default='', max_length=55),
        ),
    ]
