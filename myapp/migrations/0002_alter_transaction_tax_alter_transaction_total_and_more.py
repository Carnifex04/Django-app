# Generated by Django 4.2 on 2023-04-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tax',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='unit_price',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]