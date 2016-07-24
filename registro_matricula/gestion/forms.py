from django import forms
from .models import Materia
from .models import Alumno
import datetime

class FormMateria(forms.ModelForm):
	class Meta:
		year=range(2016,2017)
		model=Materia
		fields=['nombre','fechaInicio','fechaFin','creditos','cupos']
		widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.TextInput(attrs={'class': 'form-control'}),
            'cupos': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInicio': forms.SelectDateWidget(
		        empty_label=("Año", "Mes", "Dia"),
		        years=year,
		        attrs={'class': 'form-control'},
		    ),
		    'fechaFin': forms.SelectDateWidget(
		        empty_label=("Año", "Mes", "Dia"),
		        years=year,
		        attrs={'class': 'form-control'},
		    ),
        }


class FormAlumno(forms.ModelForm):
	class Meta:
		esteAño=datetime.date.today().year
		year=range(esteAño-100,esteAño+1)
		model=Alumno
		fields=['nombres','apellidos','cedula','correo','telefono','celular','direccion','sexo','fechaNacimiento']
		widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.SelectDateWidget(
		        empty_label=("Año", "Mes", "Dia"),
		        years=year,
		        attrs={'class': 'form-control'},
		    ),
        }
