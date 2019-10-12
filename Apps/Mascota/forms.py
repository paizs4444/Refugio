from django import forms
from Apps.Mascota.models import Mascota, Vacuna

class MascotaForm(forms.ModelForm):

     class Meta:
         model = Mascota

         fields = [
         'Nombre',
         'Sexo',
         'Edad_aproximada',
         'Fecha_rescate',
         'Persona',
         'Vacuna',
         ]

         labels = {
         'Nombre':'Nombre',
         'Sexo':'Sexo',
         'Edad_aproximada':'Edad aproximada',
         'Fecha_rescate':'Fecha del rescate',
         'Persona':'Adoptante',
         'Vacuna':'Vacuna',
         }

         widgets = {
         'Nombre': forms.TextInput(attrs={'class':'form-control'}),
         'Sexo': forms.Select(attrs={'class':'form-control'}),
         'Edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
         'Fecha_rescate': forms.SelectDateWidget(years=range(1990,2050), attrs={'class':'form-control'}),
         'Persona': forms.Select(attrs={'class':'form-control'}),
         'Vacuna': forms.CheckboxSelectMultiple(),
         }

class VacunaForm(forms.ModelForm):

		class Meta:
				model = Vacuna
				fields = [
					'Nombre'
				]
				labels = {
					'Nombre': 'Nombre de vacuna',

				}
				widgets = {
					'Nombre':forms.TextInput(attrs={'class':'form-control'}),
				}
