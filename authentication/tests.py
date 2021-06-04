from django.contrib.auth.forms import UsernameField
from django.test import TestCase, Client
from authentication.models import User, Doctor

# Create your tests here.
class AuthenticationTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="pavlo", password="123", email="pavlo@gmail.com", first_name="Pavlo", last_name="Kahitin")
        doctor = User.objects.create(username="maksym", password="123", email="hrynak@gmail.com", first_name="Maksym", last_name="Hrynak")
        Doctor.objects.create(user=doctor, bio="Surgery", location="Novoyavorivsk")

    def test_if_user_can_sign_up(self):
        c = Client()
        response = c.post("/auth/sign-up/", {'username': 'pavlo', 'password': '123', 'password2': '123', 'email': 'pavlo@gmail.com'})
        self.assertEqual(response.status_code, 200)

    def test_if_doctor_can_sign_up(self):
        c = Client()
        response = c.post("/auth/sign-up/", {'username': 'maksym', 'password': '123', 'password2': '123', 'email': 'maksym@gmail.com'})
        self.assertEqual(response.status_code, 200)

    def test_if_doctor_can_login(self):
        c = Client()
        response = c.post("/auth/sign-in/", {'username': 'pavlo', 'password': '123'})
        self.assertEqual(response.status_code, 200)

    def test_if_doctor_can_login(self):
        c = Client()
        response = c.post("/auth/sign-in/", {'username': 'maksym', 'password': '123'})
        self.assertEqual(response.status_code, 200)

    def test_if_user_exists(self):
        user_pavlo= User.objects.get(username="pavlo")
        self.assertEqual(user_pavlo.first_name, "Pavlo")
        self.assertEqual(user_pavlo.last_name, "Kahitin")
        self.assertEqual(user_pavlo.email, "pavlo@gmail.com")

    def test_if_doctor_exists(self):
        doctor_maksym = Doctor.objects.get(user=User.objects.get(username="maksym"))
        self.assertEqual(doctor_maksym.user.first_name, "Maksym")
        self.assertEqual(doctor_maksym.user.last_name, "Hrynak")
        self.assertEqual(doctor_maksym.user.email, "hrynak@gmail.com")
        self.assertEqual(doctor_maksym.bio, "Surgery")
        self.assertEqual(doctor_maksym.location, "Novoyavorivsk")
