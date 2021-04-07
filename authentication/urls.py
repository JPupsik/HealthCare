from django.conf.urls import url

from authentication.views import SignInView, SignUpView

urlpatterns = [
    url('sign-in', SignInView.as_view()),
    url('sign-up', SignUpView.as_view()),
]
