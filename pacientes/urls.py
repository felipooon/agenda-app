from django.urls import path
from . import views


urlpatterns = [
    path("nuevo/", views.crear_paciente, name="crear_paciente"),
    path("", views.lista_pacientes, name="lista_pacientes"),
    path("<int:id>/", views.detalle_paciente, name='detalle_paciente'),
]