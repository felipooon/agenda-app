from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    notas = models.TextField(blank=True)
    nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
def total_reservas(self):
    return self.reserva_set.count()

def asistencias(self):
    return self.reserva_set.filter(estado="asistio").count()