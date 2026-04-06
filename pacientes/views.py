from django.shortcuts import render, redirect
from .forms import PacienteForm

def crear_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("agenda_hoy")

    else:
        form = PacienteForm()

    return render(request, "pacientes/crear_paciente.html", {"form": form})