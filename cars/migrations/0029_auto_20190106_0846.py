# Generated by Django 2.1.5 on 2019-01-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0028_auto_20190106_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='image',
            field=models.ImageField(blank=True, default='/car_images/default.png', upload_to='car_images/', verbose_name='Nuotrauka'),
        ),
    ]
