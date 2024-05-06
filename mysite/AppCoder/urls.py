from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('asignarActivos', views.asignarActivos, name="guardar_activos"),
    path('usuarios', views.asignarUsuarios, name="guardar_usuario"),
    path('activos', views.asignarTipoActivos, name="guardar_tipo_activo"),
    path('busqueda', views.buscar_activos, name="buscar_activos"),
    path('buscar/', views.busqueda_activo)
]