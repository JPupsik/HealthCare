from django.http import Http404
from django.shortcuts import render

from authentication.models import Doctor


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


def make_reservation(request, doc_id):
    try:
        doctor = Doctor.objects.get(pk=doc_id)
    except Doctor.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'reservation.html', {'doctor': doctor})
