from django.shortcuts import redirect, render

# Create your views here.
import pandas as pd
from django.shortcuts import render

from dateutil import parser
from .models import Transaction

# uploads the csv to the database


def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']

        # creating dataframe
        df = pd.read_csv(csv_file)

        # cleaning the dataframe with only the columns required,
        # and extracting the first 60 columns
        df = df[['Invoice ID', 'Product line', 'Unit price',
                 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time']][:60]
        for index, row in df.iterrows():
            # creating an instance of the Transaction Model with all the required fields
            transaction = Transaction(
                invoice_id=row['Invoice ID'],
                product_line=row['Product line'],
                unit_price=row['Unit price'],
                quantity=row['Quantity'],
                tax=row['Tax 5%'],
                total=row['Total'],
                # parsing the date as the dates in the csv contained dates in varied forms
                date=parser.parse(row['Date']).strftime('%Y-%m-%d'),
                time=row['Time']
            )
            # saving the transaction in the database
            transaction.save()
        # redirecting to the transaction view to show all the transactions
        return redirect('/transactions')
    return render(request, 'upload_csv.html')


# filters and returns a list of transactions
def transactions(request):
    transactions = Transaction.objects.filter(
        product_line='Health and beauty')
    # callback to the transactions.html file and passing the transaction query
    return render(request, 'transactions.html', {'transactions': transactions})
