from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from Apps.Mascota.views import Index, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete,\
 VacunaList, VacunaCreate, VacunaUpdate, VacunaDelete

app_name = 'mascota'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('nuevo', MascotaCreate.as_view(), name='mascota_crear'),
    path('listar', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:pk>', MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<int:pk>', MascotaDelete.as_view(), name='mascota_eliminar'),

    path('Vnuevo', VacunaCreate.as_view(), name='vacuna_crear'),
    path('Vlistar', VacunaList.as_view(), name='vacuna_listar'),
    path('Veditar/<int:pk>', VacunaUpdate.as_view(), name='vacuna_editar'),
    path('Veliminar/<int:pk>', VacunaDelete.as_view(), name='vacuna_eliminar'),
]
