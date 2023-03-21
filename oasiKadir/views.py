from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import CreateReservation
from .models import Reservation


# Create your views here.
def reservation(response):
    if response.method == "POST":
        form = CreateReservation(response.POST)
        if form.is_valid():
            reservation = Reservation(
                date=form.cleaned_data['date'],
                cena=form.cleaned_data['cena'],
                pranzo=form.cleaned_data['pranzo'],
                adults=form.cleaned_data['adults'],
                children=form.cleaned_data['children'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                note=form.cleaned_data['note'],
            )
            reservation.save()
            return redirect('home')
    else:
        initial_data = {}
        date_param = response.GET.get("date")
        if date_param:
            initial_data['date'] = date_param
        form = CreateReservation(initial=initial_data)
    return render(response, "oasiKadir/reservation.html", {"form": form})

def home(response):
    reservations = Reservation.objects.all()
    return render(response, "oasiKadir/home.html", {'reservations': reservations})

