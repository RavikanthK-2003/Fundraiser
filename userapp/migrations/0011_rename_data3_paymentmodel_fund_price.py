# Generated by Django 4.0.3 on 2022-04-07 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_paymentmodel_data3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmodel',
            old_name='data3',
            new_name='fund_price',
        ),
    ]
