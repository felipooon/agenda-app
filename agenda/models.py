from django.db import models
from pacientes.models import Paciente
from django.core.exceptions import ValidationError
from datetime import datetime

class Reserva(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.IntegerField(default=30)  # duración en minutos

    ESTADOS = [
        ("reservado", "Reservado"),
        ("asistio", "Asistió"),
        ("no_asistio", "No asistió"),
    ]

    estado = models.CharField(max_length=20, choices=ESTADOS, default="reservado")

    def clean(self):
        fecha_hora = datetime.combine(self.fecha, self.hora)
        if fecha_hora < datetime.now():
            raise ValidationError("No puedes agendar una reserva en el pasado")

        if Reserva.objects.filter(fecha=self.fecha, hora=self.hora).exclude(pk=self.pk).exists():
            raise ValidationError("Ya hay una reserva para esa hora")    

    def __str__(self):
        return f"{self.paciente} - {self.fecha} {self.hora}"
