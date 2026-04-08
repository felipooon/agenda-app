from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True, null=True, blank=True)

    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    notas = models.TextField(blank=True)
    nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}".strip()
    
def total_reservas(self):
    return self.reserva_set.count()

def asistencias(self):
    return self.reserva_set.filter(estado="asistio").count()