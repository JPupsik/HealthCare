from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from authentication.models import Doctor
from reservations.forms import ReservationForm
from reservations.models import Reservation


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


def reservation_list(request):
    user = request.user
    reservations = Reservation.objects.filter(client=user)
    return render(request, 'my-reservations.html', {'reservations': reservations})


class ReservationView(View):
    form_class = ReservationForm

    def get(self, request, doc_id):
        user = self.request.user
        try:
            doctor = Doctor.objects.get(pk=doc_id)
        except Doctor.DoesNotExist:
            raise Http404("Reservation does not exist")
        return render(request, 'reservation.html', {'doctor': doctor, 'form': self.form_class})

    def post(self, request, doc_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            doctor = Doctor.objects.get(pk=doc_id)
            reservation = Reservation()
            reservation.client = request.user
            reservation.doctor = doctor
            reservation.time = form.cleaned_data['time']
            reservation.date = form.cleaned_data['date']
            reservation.save()
            return HttpResponseRedirect('/reservations/')

        return render(request, 'reservation.html', {'form': form})


class ReservationDelete(DeleteView):
    model = Reservation
    template_name = 'delete_reservation.html'
    success_url = '/reservations/'
