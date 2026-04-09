from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

class UserTestCase(TestCase):

    def setUp(self):
        self.volunteer = User.objects.create_user(
            first_name='John',
            last_name='Wick',
            username='JWick',
            email='johnwick@gmail.com',
            password='johnwick1234',
            has_pets=True
        )

        self.staff_member = User.objects.create_user(
            first_name='Jane',
            last_name='Doe',
            username='JDoe',
            email='janedoe@gmail.com',
            role='SM',
            has_pets=False
        )

    def test_volunteer_creation(self):
        self.assertTrue(User.objects.filter(username='JWick').exists())

    def test_staff_member_creation(self):
        self.assertTrue(User.objects.filter(username='JDoe').exists())

    def test_user_str(self):
        self.assertEqual(str(self.volunteer), 'John Wick (johnwick@gmail.com)')
        self.assertEqual(str(self.staff_member), 'Jane Doe (janedoe@gmail.com)')

    def test_no_empty_str_first_name(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                first_name='',
                last_name='surname',
                username='noname',
                email='noname@gmail.com',
                has_pets=False
            )

    def test_no_empty_str_last_name(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                first_name='name',
                last_name='',
                username='nosurname',
                email='nosurname@gmail.com',
                has_pets=False
            )

    def test_not_unique_username(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                first_name='Blaine',
                last_name='Tyrrell',
                username='JWick',
                email='blainetyrrell@gmail.com',
                has_pets=True
            )

    def test_not_unique_email(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                first_name='Neville',
                last_name='Fabian',
                username='NFabian',
                email='johnwick@gmail.com',
                has_pets=False
            )

    def test_volunteer_as_default(self):
        self.assertEqual(self.volunteer.role, 'V')

    def test_password_is_hashed(self):
        self.assertNotEqual(self.volunteer.password, 'johnwick1234')
        self.assertTrue(self.volunteer.check_password('johnwick1234'))
