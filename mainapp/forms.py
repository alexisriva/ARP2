from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name','cedula',]#'goesToVisit',]
        labels = {
            'name': 'Nombre del visitante',
            'cedula': 'Cedula del visitante',
            #'goesToVisit': 'Invitado por'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'id': 'cedula'}),
            #'goesToVisit': forms.Select()
        }
