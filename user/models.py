from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    # TODO: find a way to verify people can't simply put 'staff member'

    ROLE = (
        ('V', 'Volunteer')
        ('SM', 'Staff Member')
    )

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE)
    is_owner = models.BooleanField()

    def __str__(self):
        return self.username
