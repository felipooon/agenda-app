from django.db import models

# Create your models here.

from django.db import models
from pacientes.models import Paciente

class Reserva(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    ESTADOS = [
        ("reservado", "Reservado"),
        ("asistio", "Asistió"),
        ("no_asistio", "No asistió"),
    ]

    estado = models.CharField(max_length=20, choices=ESTADOS, default="reservado")

    def __str__(self):
        return f"{self.paciente} - {self.fecha} {self.hora}"
