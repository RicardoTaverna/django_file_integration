from django import forms
"""Arquivo para criar os formularios referente ao app integration."""
from django.forms import fields
from integration.models import Documento

class DocumentForm(forms.ModelForm):
    """Classe para gerar o formulário."""
    class Meta:
        model = Documento
        fields = ('descricao', 'documento',)