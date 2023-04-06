from django.urls import path
from .views import upload_csv, transactions

# redirected urls
# '' redirects to the upload_csv view used for uploading the csv file
# 'transactions' redirects to the transactions view which shows all the required transactions
urlpatterns = [
    path('', upload_csv, name='upload_csv'),
    path('transactions/', transactions, name='transactions'),
]
