# Generated by Django 2.1 on 2019-02-23 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0046_auto_20190223_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='selected_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='selected_car_name', to='cars.CarDetails', verbose_name='PasirinktiAutomobili'),
        ),
    ]
