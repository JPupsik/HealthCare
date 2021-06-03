from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from HealthCare.views import IndexView
from reservations.views import doctor_list, ReservationView, reservation_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('doctors/', doctor_list, name='doctor_list'),
    path('reservations/', reservation_list, name='reservation_list'),
    path('make-reserve/<int:doc_id>/', ReservationView.as_view(), name='make_reservation'),
    url('', IndexView.as_view())
]
