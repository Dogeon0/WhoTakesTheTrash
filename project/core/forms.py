from django import forms
from . import models

class AgregarMensaje(forms.ModelForm):
    class Meta:
        model = models.Mensaje
        fields = "__all__"

class MostrarMensajes(forms.Form):
    query = forms.CharField(label='Mensaje')