from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from Apps.Adopcion.views import SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

app_name = 'adopcion'
urlpatterns = [
    # pat(r'index$', index_adopcion),
     path('listar', SolicitudList.as_view(), name='solicitud_listar'),
     path('nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
     path('editar/<int:pk>', SolicitudUpdate.as_view(), name='solicitud_editar'),
     path('eliminar/<int:pk>', SolicitudDelete.as_view(), name='solicitud_eliminar'),

]
