from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Reserva
from datetime import date

def agenda_hoy(request):
    hoy = date.today()
    reservas = Reserva.objects.filter(fecha=hoy).order_by("hora")

    return render(request, "agenda/agenda_hoy.html", {
        "reservas": reservas,
        "hoy": hoy
    })

def marcar_asistio(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.estado = "asistio"
    reserva.save()
    return redirect("agenda_hoy")  # vuelve a la agenda

def marcar_no_asistio(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.estado = "no_asistio"
    reserva.save()
    return redirect("agenda_hoy")  # vuelve a la agenda