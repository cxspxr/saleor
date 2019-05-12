from django import forms
from django.utils.translation import pgettext_lazy, ugettext_lazy as _

from ... import ChargeStatus


class TelegramPaymentForm(forms.Form):
    charge_status =  ChargeStatus.NOT_CHARGED

    def __init__(self,*args,**kwargs):
        self.order_id = kwargs.pop('order_id')
        super(TelegramPaymentForm,self).__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = {}
        cleaned_data['charge_status'] = ChargeStatus.NOT_CHARGED

        return cleaned_data

    def get_payment_token(self):
        """Return selected charge status instead of token for testing only.
        Gateways used for production should return an actual token instead."""
        charge_status = self.cleaned_data["charge_status"]
        return charge_status
