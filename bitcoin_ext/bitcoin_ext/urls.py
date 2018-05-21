from django.contrib import admin
from django.conf.urls import url
from bitcoin_extended.views import address_view, transactions_view

urlpatterns = [
    url('admin/', admin.site.urls),
    url('address/', address_view, name="address"),
    url('transactions/', transactions_view, name="transactions")

]
