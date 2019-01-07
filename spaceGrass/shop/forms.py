# .*. coding: utf-8 .*.
from django import forms
from shop.models import Delivery, Payment

class OrderForm(forms.Form):
    email = forms.EmailField()
    delivery = forms.ModelChoiceField(queryset=Delivery.objects.all())
    payment = forms.ModelChoiceField(queryset=Payment.objects.all())

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['delivery'].label = 'Способ доставки'
        self.fields['payment'].label = 'Способ оплаты'
