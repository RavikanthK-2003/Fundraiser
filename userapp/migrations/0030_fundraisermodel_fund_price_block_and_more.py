# Generated by Django 4.1.3 on 2022-12-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0029_alter_paymentmodel_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundraisermodel',
            name='fund_price_block',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fundraisermodel',
            name='price_block',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fundraisermodel',
            name='raisefundfor_block',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
