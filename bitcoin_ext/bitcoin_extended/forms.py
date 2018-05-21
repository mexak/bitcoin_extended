from .models import Address, Times
from django.forms import ModelForm


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class TimesForm(ModelForm):
    class Meta:
        model = Times
        fields = '__all__'
