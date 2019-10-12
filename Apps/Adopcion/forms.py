from django import forms
from Apps.Adopcion.models import Persona, Solicitud
from betterforms.multiform import MultiModelForm
# instalamos pip install django-betterforms

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields = [
			'Nombre',
			'Apellido',
			'Edad',
			'Telefono',
			'Email',
			'Domicilio',
		]
		labels = {
			'Nombre': 'Nombre',
			'Apellido': 'Apellidos',
			'Edad': 'Edad',
			'Telefono': 'Teléfono',
			'Email': 'Correo electrónico',
			'Domicilio': 'Domicilio',
		}
		widgets = {
			'Nombre':forms.TextInput(attrs={'class':'form-control'}),
			'Apellido':forms.TextInput(attrs={'class':'form-control'}),
			'Edad':forms.TextInput(attrs={'class':'form-control'}),
			'Telefono':forms.TextInput(attrs={'class':'form-control'}),
			'Email':forms.TextInput(attrs={'class':'form-control'}),
			'Domicilio':forms.Textarea(attrs={'class':'form-control'}),
		}


class SolicitudForm(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = [
			'Numero_mascotas',
			'Razones',
		]
		labels = {
			'Numero_mascotas': 'Numero de mascotas',
			'Razones': 'Razones para adoptar',

		}
		widgets = {
			'Numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
			'Razones':forms.Textarea(attrs={'class':'form-control'}),
		}
