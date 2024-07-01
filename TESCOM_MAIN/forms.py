from django import forms
<<<<<<< Updated upstream

class FechaForm(forms.Form):
    fecha = forms.DateField(required=False, widget=forms.DateInput(format='%Y-%m-%d'))
=======
from .models import TrabajoTerminal, Profesor


class TrabajoTerminalForm(forms.ModelForm):
    alumno_id = forms.IntegerField(label='Numero de Boleta')

    profesores = forms.ModelMultipleChoiceField(
        queryset=Profesor.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = TrabajoTerminal
        fields = ['tt_id', 'titulo', 'descripcion', 'archivo', 'profesores']
>>>>>>> Stashed changes
