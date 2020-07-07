from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class Subscriber(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    first_name = models.CharField(max_length=50,validators=[alphanumeric,MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, validators=[alphanumeric,MinLengthValidator(2)])
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name 