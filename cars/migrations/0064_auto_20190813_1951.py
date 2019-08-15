# Generated by Django 2.1.5 on 2019-08-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0063_auto_20190813_1900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardetails',
            options={'verbose_name_plural': 'Car Description'},
        ),
        migrations.AlterModelOptions(
            name='carimage',
            options={'verbose_name_plural': 'Car Images'},
        ),
        migrations.AlterModelOptions(
            name='carmake',
            options={'verbose_name_plural': 'Car Make'},
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='kebuloTipas',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Station Wagon', 'Station Wagon'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Minivan', 'Minivan'), ('Other', 'Other')], default='Sedanas', max_length=25),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='kuroTipas',
            field=models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Electric', 'Electric')], default='Benzinas', max_length=25),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='alt_text',
            field=models.CharField(choices=[('Front', 'Front'), ('Back', 'Back'), ('Side', 'Side'), ('Inside', 'Inside'), ('Paperwork', 'Paperwork'), ('Other', 'Other')], default='Kita', max_length=200, null=True, verbose_name='Papildomas_Tekstas'),
        ),
        migrations.AlterField(
            model_name='carmake',
            name='car_make',
            field=models.CharField(max_length=200, verbose_name='Car Make'),
        ),
    ]
