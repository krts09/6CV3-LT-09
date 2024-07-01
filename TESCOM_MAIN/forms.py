from django import forms

class FechaForm(forms.Form):
    fecha = forms.DateField(required=False, widget=forms.DateInput(format='%Y-%m-%d'))
