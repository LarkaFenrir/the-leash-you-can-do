from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q, CheckConstraint
from django.core.exceptions import ValidationError

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

        # database level validation to prevent empty strings
        constraints = [
            CheckConstraint(
                condition=~Q(first_name=''),
                name='first_name_not_empty'
            ),
            CheckConstraint(
                condition=~Q(last_name=''),
                name='last_name_not_empty'
            )
        ]

    def __str__(self):
        return f'{self.get_full_name()} ({self.email})'

    def clean(self):
        '''Catches complex invalid input like "   ".'''
        super().clean()
        if self.first_name is not None and self.first_name.strip() == '':
            raise ValidationError(
                {'first_name': 'First name cannot be empty or just spaces.'}
            )
        if self.last_name is not None and self.last_name.strip() == '':
            raise ValidationError(
                {'last_name': 'Last name cannot be empty or just spaces.'}
            )
