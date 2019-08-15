# Generated by Django 2.1.5 on 2019-03-03 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0054_carmake'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='automobilio_marke',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='automobilio_marke_name', to='cars.CarMake', verbose_name='Automobilio Markė'),
            preserve_default=False,
        ),
    ]
