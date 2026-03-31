from django.contrib import admin
from .models import Reserva

# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "fecha", "hora", "estado")
    list_filter = ("fecha", "estado")
    search_fields = ("paciente__nombre",)
