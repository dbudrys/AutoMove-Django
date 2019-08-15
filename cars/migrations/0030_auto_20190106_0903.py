# Generated by Django 2.1.5 on 2019-01-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    
    dependencies = [
        ('cars', '0029_auto_20190106_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='duruSkaicius',
            field=models.CharField(choices=[('2/3', '2/3'), ('4/5', '4/5'), ('Kita', 'Kita')], default='4/5', max_length=10, verbose_name='Prekyboje?'),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='image',
            field=models.ImageField(blank=True, default='/car_images/default.png', upload_to='car_images/', verbose_name='PragrindineNuotrauka'),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='kaina',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='pagaminimoMenuo',
            field=models.CharField(choices=[('', ''), ('-01', '01'), ('-02', '02'), ('-03', '03'), ('-04', '04'), ('-05', '05'), ('-06', '06'), ('-07', '07'), ('-08', '08'), ('-09', '09'), ('-10', '10'), ('-11', '11'), ('-12', '12')], default='', max_length=25, null=True),
        ),
    ]
