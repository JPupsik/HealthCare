import datetime

from reservations.views import doctor_list, reservation_list
from django.test import TestCase, Client
from reservations.models import Doctor, User, Reservation

# Create your tests here.
class ReservationTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="pavlo", password="123", email="pavlo@gmail.com", first_name="Pavlo", last_name="Kahitin")
        doctor_user = User.objects.create(username="maksym", password="123", email="hrynak@gmail.com", first_name="Maksym", last_name="Hrynak")
        doctor = Doctor.objects.create(user=doctor_user, bio="Surgery", location="Novoyavorivsk")
        reservation = Reservation.objects.create(doctor=doctor, client=user, time=datetime.time(10, 30, 0), date= datetime.date(2021, 6, 4))

    def test_check_if_reservation_is_creating(self):
        c = Client()
        response = c.post("/make-reserve/1/", {'date': '2021 6 4', 'time': '10:30'})
        self.assertEqual(response.status_code, 200)
    
    def test_error_not_such_reservation(self):
        c = Client()
        response = c.get("/make-reserve/2/")
        self.assertNotEqual(response.status_code, 200)
        
