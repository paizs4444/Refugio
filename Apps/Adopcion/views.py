from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
from Apps.Adopcion.forms import SolicitudForm, PersonaForm
from Apps.Adopcion.models import Persona, Solicitud
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SolicitudList(LoginRequiredMixin, ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'
	paginate_by = 5

class SolicitudCreate(LoginRequiredMixin, CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.Persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(LoginRequiredMixin, UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')

	def get_context_data(self, **kwargs):
		    context = super(SolicitudUpdate, self).get_context_data(**kwargs)
		    pk = self.kwargs.get('pk', 0)
		    solicitud = self.model.objects.get(id=pk)
		    persona = self.second_model.objects.get(id=solicitud.Persona_id)
		    if 'form' not in context:
		    	context['form'] = self.form_class()
		    if 'form2' not in context:
		    	context['form2'] = self.second_form_class(instance=persona)
		    context['id'] = pk
		    return context

	def post(self, request, *args, **kwargs):
			self.object = self.get_object
			id_solicitud = kwargs['pk']
			Solicitud = self.model.objects.get(id=id_solicitud)
			Persona = self.second_model.objects.get(id=Solicitud.Persona_id)
			form = self.form_class(request.POST, instance=Solicitud)
			form2 = self.second_form_class(request.POST, instance=Persona)
			if form.is_valid() and form2.is_valid():
				form.save()
				form2.save()
				return HttpResponseRedirect(self.get_success_url())
			else:
				return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(LoginRequiredMixin, DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitud_delete.html'
	success_url = reverse_lazy('adopcion:solicitud_listar')
