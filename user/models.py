from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """Custom user model for shelter members.

    Features:
    - every field is required
    - email is a unique field and it is required to login
    """
    ROLE_CHOICES = (
        ('V', 'Volunteer'),
        ('SM', 'Staff Member')
    )

    # add first_name and last_name to make them required
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)

    # inherit the password to hash it, improving security

    email = models.EmailField(unique=True)

    # paired with omitting the choice in the form
    # only admin can change a user's role from their admin panel
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='V')

    has_pets = models.BooleanField(
        default=False,
        help_text='Do you own any pets?'
    )

    # users will use email instead of username as login info
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        verbose_name = 'Shelter Member'
        verbose_name_plural = 'Shelter Members'

    def __str__(self):
        return f'{self.get_full_name()} ({self.email})'
