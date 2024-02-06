from django.db import models
from django.core.validators import RegexValidator


class GuestForm(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)  # Use DateTimeField instead of TimeField for both date and time
    entering = models.BooleanField()  # Use a.py more descriptive name for the field
    roll_id = models.CharField(max_length=200)  # Use snake_case for variable names
    contact = models.CharField(max_length=10,
                               validators=[RegexValidator(regex='^\d{10}$', message='Contact must be 10 digits')])
    address = models.CharField(max_length=500)
    purpose = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
