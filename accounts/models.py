from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11)
    id_number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    id_copy = models.FileField(upload_to='accounts/id_copy/')
    proof_of_address = models.FileField(upload_to='accounts/address_copy/')
