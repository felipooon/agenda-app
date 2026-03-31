from django.urls import path
from . import views

urlpatterns = [
    path("", views.agenda_hoy, name="agenda_hoy"),
    path("reserva/<int:reserva_id>/asistio/", views.marcar_asistio, name="marcar_asistio"),
    path("reserva/<int:reserva_id>/no_asistio/", views.marcar_no_asistio, name="marcar_no_asistio"),
]
