from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from HealthCare.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    url('', IndexView.as_view())
]
