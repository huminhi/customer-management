from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms

from src.core.models import Customer


def validate_phone(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

