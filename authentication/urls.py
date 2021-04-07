from django.urls import path

from authentication.views import CustomLoginView, RegisterView, CustomLogOutView

urlpatterns = [
    path('sign-in/', CustomLoginView.as_view(), name='login'),
    path('log-out/', CustomLogOutView.as_view(), name='logout'),
    path('sign-up/', RegisterView.as_view(), name='signup'),
]
