# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-02 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0020_cardetails_kad'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='kad22',
            field=models.TextField(blank=True, null=True),
        ),
    ]
