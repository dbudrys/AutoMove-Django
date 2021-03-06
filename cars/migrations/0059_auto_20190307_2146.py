# Generated by Django 2.1.5 on 2019-03-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0058_auto_20190303_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='prekyboje',
            field=models.CharField(choices=[('Parduodama', 'Parduodama'), ('Parduota', 'Parduota'), ('Rezervuota', 'Rezervuota'), ('Kita', 'Kita (susisiekite)')], default='Parduodama', max_length=10, verbose_name='Prekyboje?'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='alt_text',
            field=models.CharField(choices=[('Priekis', 'Priekis'), ('Galas', 'Galas'), ('Šonas', 'Šonas'), ('Salonas', 'Salonas'), ('Dokumentai', 'Dokumentai'), ('Kita', 'Kita')], default='Kita', max_length=200, null=True, verbose_name='Papildomas_Tekstas'),
        ),
    ]
