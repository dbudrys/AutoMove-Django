# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-02 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='iamge',
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=1, upload_to='car_images/'),
            preserve_default=False,
        ),
    ]
