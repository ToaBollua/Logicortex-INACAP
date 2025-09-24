from django import forms

class RespuestaForm(forms.Form):
    respuesta = forms.CharField(label='Tu respuesta', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
