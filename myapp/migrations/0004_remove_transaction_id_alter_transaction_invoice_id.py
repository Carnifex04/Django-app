# Generated by Django 4.2 on 2023-04-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_transaction_tax_alter_transaction_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]