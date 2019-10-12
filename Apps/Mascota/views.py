from django import forms
from django.shortcuts import render, redirect
from Apps.Mascota.forms import MascotaForm, VacunaForm
from Apps.Mascota.models import Mascota, Vacuna
from django.views.generic import TemplateView , ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Index( ListView):
	model = Mascota
	template_name = 'mascota/index.html'

class MascotaList(LoginRequiredMixin, ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'
	paginate_by = 5

class MascotaCreate(LoginRequiredMixin, CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')


class MascotaUpdate(LoginRequiredMixin, UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')


class MascotaDelete(LoginRequiredMixin, DeleteView):
	model = Mascota
	template_name = 'mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_listar')

class VacunaList(LoginRequiredMixin, ListView):
		model = Vacuna
		template_name = 'vacuna/vacuna_list.html'
		paginate_by = 5

class VacunaCreate(LoginRequiredMixin, CreateView):
		model = Vacuna
		form_class = VacunaForm
		template_name = 'vacuna/vacuna_form.html'
		success_url = reverse_lazy('mascota:vacuna_listar')


class VacunaUpdate(LoginRequiredMixin, UpdateView):
		model = Vacuna
		form_class = VacunaForm
		template_name = 'vacuna/vacuna_form.html'
		success_url = reverse_lazy('mascota:vacuna_listar')



class VacunaDelete(LoginRequiredMixin, DeleteView):
		model = Vacuna
		template_name = 'vacuna/vacuna_delete.html'
		success_url = reverse_lazy('mascota:vacuna_listar')
