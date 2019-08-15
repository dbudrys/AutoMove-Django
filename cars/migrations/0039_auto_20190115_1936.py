# Generated by Django 2.1.5 on 2019-01-15 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0038_auto_20190115_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carimage',
            name='image_file',
        ),
        migrations.AddField(
            model_name='carimage',
            name='selected_car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selected_car_name', to='cars.CarDetails', verbose_name='hello'),
            preserve_default=False,
        ),
    ]
