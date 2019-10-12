from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'password1',
				'password2',
				'first_name',
				'last_name',
				'email',

			]
		labels = {
				'username':'Nombre de usuario',
				'password1':'Contraseña',
				'password2':'Confirmar Contraseña',
				'first_name':'Nombre',
				'last_name':'Apellidos',
				'email':'Correo',
		          }

		widgets = {
                'username':forms.TextInput(attrs={'class':'form-control'}),
			    'password1':forms.TextInput(attrs={'class':'form-control'}),
			    'password2':forms.TextInput(attrs={'class':'form-control'}),
			    'first_name':forms.TextInput(attrs={'class':'form-control'}),
			    'last_name':forms.TextInput(attrs={'class':'form-control'}),
			    'email':forms.EmailInput(attrs={'class':'form-control'}),
				  }
