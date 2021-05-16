from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from HealthCare.views import IndexView
from reservations.views import doctor_list, make_reservation

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('doctors/', doctor_list, name='doctor_list'),
    path('make-reserve/<int:doc_id>/', make_reservation, name='make_reservation'),
    url('', IndexView.as_view())
]
