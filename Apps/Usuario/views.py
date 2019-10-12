from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View , TemplateView , CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


from Apps.Usuario.forms import RegistroForm

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')

def get_form_kwargs(self, *args, **kwargs):
	     kwargs = super(RegistroUsuario, self).get_form_kwargs(
	         *args, **kwargs)
	     return kwargs
