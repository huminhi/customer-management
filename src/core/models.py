import uuid
from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, )
    phone = models.CharField(max_length=11, null=True, unique=True,
                             validators=[RegexValidator(regex='^\d{11}$',
                                                        message='Phone number contains 11 digits only')])
    modified_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
