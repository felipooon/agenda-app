from datetime import date
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm
from .models import Paciente, NotaPaciente
from agenda.models import Reserva
from django.db.models import Count, Q

def crear_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("agenda_hoy")

    else:
        form = PacienteForm()

    return render(request, "pacientes/crear_paciente.html", {"form": form})

def lista_pacientes(request):
    query = request.GET.get("q", "")

    pacientes = Paciente.objects.all()

    if query:
        pacientes = Paciente.objects.filter(
            Q(rut__icontains=query) |
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(nombre__icontains=query.split()[0]) if query.split() else Q()  # Primera palabra
        ).distinct()

    pacientes = pacientes.annotate(
        total_reservas=Count('reserva'),
        asistencias=Count('reserva', filter=Q(reserva__estado="asistio"))
    ).order_by("apellido", "nombre")  # ahora ordenado por apellido

    return render(request, "pacientes/lista_pacientes.html", {
        "pacientes": pacientes
    })

def cumpleanos_hoy(request):
    hoy = date.today()

    pacientes = Paciente.objects.filter(
        nacimiento__day=hoy.day,
        nacimiento__month=hoy.month
    )

    return render(request, "pacientes/cumpleanos.html", {
        "pacientes": pacientes
    })

def buscar_pacientes(request):
    query = request.GET.get("q", "")
    pacientes = Paciente.objects.filter(
        Q(nombre__icontains=query) | Q(apellido__icontains=query)
    )[:10]

    # Devuelve nombre completo
    data = [
        {"id": p.id, "nombre": p.nombre, "apellido": p.apellido}
        for p in pacientes
    ]
    return JsonResponse(data, safe=False)

def detalle_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == "POST":
        contenido = request.POST.get("contenido")

        if contenido:
            NotaPaciente.objects.create(
                paciente=paciente,
                contenido=contenido
            )

        return redirect('detalle_paciente', id=paciente.id)

    notas = paciente.notas_historial.all().order_by('-fecha')

    return render(request, "pacientes/detalle_paciente.html", {
        "paciente": paciente,
        "notas": notas
    })
