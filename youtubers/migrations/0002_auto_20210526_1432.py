# Generated by Django 3.2.3 on 2021-05-26 09:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('sony', 'sony'), ('nikon', 'nikon'), ('red', 'red'), ('fuji', 'fuji'), ('panasonic', 'panasonic'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('coding', 'coding'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('cooking', 'cooking'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]