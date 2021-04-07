from django.conf.urls import url

from authentication.views import TestView

urlpatterns = [
    url('sign-in', TestView.as_view()),
]
