from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from HealthCare.views import IndexView
from reservations.views import doctor_list, ReservationView, reservation_list, ReservationDelete
app_name = 'healthcare'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('doctors/', doctor_list, name='doctor_list'),
    path('reservations/', reservation_list, name='reservation_list'),
    path('make-reserve/<int:doc_id>/', login_required(login_url='/auth/sign-in/')(ReservationView.as_view()), name='make_reservation'),
    path('reservations/<int:pk>/delete/', ReservationDelete.as_view(), name='reservation_delete'),
    url('', IndexView.as_view())
]
