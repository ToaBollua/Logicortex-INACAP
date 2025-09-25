from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class RespuestaForm(forms.Form):
    respuesta = forms.CharField(
        label='Tu respuesta',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )