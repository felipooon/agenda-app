from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Reserva
from datetime import date, timedelta
from .forms import ReservaForm
from django.http import JsonResponse
from pacientes.models import Paciente
from django.core.exceptions import ValidationError


def agenda_hoy(request):
    fecha_str = request.GET.get("fecha")
    hoy = date.today()

    cumpleanos = Paciente.objects.filter(
    nacimiento__day=hoy.day,
    nacimiento__month=hoy.month
)
    

    if fecha_str:
        fecha = date.fromisoformat(fecha_str)
    else:
        fecha = date.today()

    reservas = Reserva.objects.filter(fecha=fecha).order_by("hora")

    return render(request, "agenda/agenda_hoy.html", {
        "reservas": reservas,
        "fecha": fecha,
        "fecha_anterior": fecha - timedelta(days=1),
        "fecha_siguiente": fecha + timedelta(days=1),
        "cumpleanos": cumpleanos,
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

def agregar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)

        if form.is_valid():
            paciente_id = request.POST.get("paciente")

            # VALIDACIÓN CLAVE
            if not paciente_id:
                form.add_error(None, "Debes seleccionar un paciente válido")
            else:
                try:
                    paciente = Paciente.objects.get(pk=paciente_id)
                except Paciente.DoesNotExist:
                    form.add_error(None, "El paciente seleccionado no existe")
                else:
                    reserva = form.save(commit=False)
                    reserva.paciente = paciente

                    try:
                        reserva.full_clean()
                        reserva.save()
                        return redirect("agenda_hoy")

                    except ValidationError as e:
                        for error in e.messages:
                            form.add_error(None, error)

    else:
        form = ReservaForm()

    return render(request, "agenda/agregar_reserva.html", {"form": form})

def buscar_pacientes(request):
    query = request.GET.get("q", "")
    pacientes = Paciente.objects.filter(nombre__icontains=query)[:10]

    data = [
        {"id": p.id, "nombre": p.nombre}
        for p in pacientes
    ]

    return JsonResponse(data, safe=False)

    return render(request, "agenda/agregar_reserva.html", {"form": form})