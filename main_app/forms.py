from django.forms import ModelForm
from .models import Purchase

class PurchaseForm(ModelForm):
  class Meta:
    model = Purchase
    fields = ['purchasedate', 'purchasetime']