# Generated by Django 2.1.5 on 2019-01-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0027_auto_20190106_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='image',
            field=models.ImageField(blank=True, default='/images/default.png', upload_to='images/'),
        ),
    ]
