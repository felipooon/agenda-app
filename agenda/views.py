from django.shortcuts import render
from .models import Reserva
from datetime import date

def agenda_hoy(request):
    hoy = date.today()
    reservas = Reserva.objects.filter(fecha=hoy).order_by("hora")

    return render(request, "agenda/agenda_hoy.html", {
        "reservas": reservas,
        "hoy": hoy
    })
