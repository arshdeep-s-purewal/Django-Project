# Generated by Django 4.1.7 on 2023-03-21 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apna_bazaar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apnabazaar',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='apnabazaar',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='apnabazaar',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]