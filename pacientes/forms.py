from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False
    )

    class Meta:
        model = Paciente
        fields = ["nombre", "telefono", "email", "notas", "nacimiento"]