from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from Apps.Usuario.views import RegistroUsuario
app_name = 'usuario'
urlpatterns = [
	path('registrar', RegistroUsuario.as_view(), name="registrar"),

]
