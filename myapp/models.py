from django.db import models

# Create your models here.


class Transaction(models.Model):
    invoice_id = models.CharField(max_length=50, primary_key=True)
    product_line = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=4)
    quantity = models.IntegerField()
    tax = models.DecimalField(max_digits=10, decimal_places=4)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()
    time = models.TimeField()
