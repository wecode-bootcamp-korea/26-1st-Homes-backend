# Generated by Django 3.2.9 on 2021-11-09 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='color',
            new_name='colors',
        ),
        migrations.RenameField(
            model_name='productgroup',
            old_name='discount_price',
            new_name='discount_rate',
        ),
    ]