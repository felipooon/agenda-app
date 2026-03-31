from django.db import models
from pacientes.models import Paciente
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils import timezone

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
        #fecha_hora = datetime.combine(self.fecha, self.hora)
        #if fecha_hora < datetime.now():
            #raise ValidationError("No puedes agendar una reserva en el pasado")

        #if Reserva.objects.filter(fecha=self.fecha, hora=self.hora).exclude(pk=self.pk).exists():
            #raise ValidationError("Ya hay una reserva para esa hora")    
        # Convertir fecha+hora en datetime consciente de zona
        fecha_hora_inicio = datetime.combine(self.fecha, self.hora)
        fecha_hora_inicio = timezone.make_aware(fecha_hora_inicio, timezone.get_current_timezone())
        fecha_hora_fin = fecha_hora_inicio + timedelta(minutes=self.duracion)

        # Validar que no sea en el pasado
        if fecha_hora_inicio < timezone.now():
            raise ValidationError("No puedes agendar una reserva en el pasado")

        # Validar que no haya otra reserva exactamente a la misma hora
        if Reserva.objects.filter(fecha=self.fecha, hora=self.hora).exclude(pk=self.pk).exists():
            raise ValidationError("Ya hay una reserva para esa hora")

        # Validar solapamiento con otras reservas 
        reservas = Reserva.objects.filter(fecha=self.fecha).exclude(pk=self.pk)
        for r in reservas:
            r_inicio = datetime.combine(r.fecha, r.hora)
            r_inicio = timezone.make_aware(r_inicio, timezone.get_current_timezone())
            r_fin = r_inicio + timedelta(minutes=r.duracion)

            if fecha_hora_inicio < r_fin and fecha_hora_fin > r_inicio:
                raise ValidationError(f"Horario solapado con {r.paciente} ({r_inicio.time()} - {r_fin.time()})")
            

    def __str__(self):
        return f"{self.paciente} - {self.fecha} {self.hora}"
