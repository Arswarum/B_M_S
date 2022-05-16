# Generated by Django 4.0.4 on 2022-05-13 10:24

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=20, verbose_name='Miejscowość'),
        ),
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(default='', max_length=50, verbose_name='Adres'),
        ),
        migrations.AddField(
            model_name='user',
            name='zgoda1',
            field=models.BooleanField(default=False, verbose_name='Wyrażam zgodę na otrymanie na podany przeze mnie w formularzu adres e-mail oraz numer telefonu informacji w zakresie związanym ze zlożona rezerwacje przeze mnie'),
        ),
        migrations.AddField(
            model_name='user',
            name='zgoda2',
            field=models.BooleanField(default=False, verbose_name='Zapoznałem się z Regulaminem i akceptuję jego postanowienia'),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(default='', max_length=6, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=15, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=15, verbose_name='Nazwisko'),
        ),
    ]
