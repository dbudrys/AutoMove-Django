# Generated by Django 2.1.5 on 2019-03-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0057_auto_20190303_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmake',
            name='car_make',
            field=models.CharField(max_length=200, verbose_name='Automobilio Markė'),
        ),
    ]
