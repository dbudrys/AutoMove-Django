# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-02 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20190102_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardetails',
            name='masinosTipas',
        ),
    ]
