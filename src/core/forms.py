from django import forms

from src.core.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
