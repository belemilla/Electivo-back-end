# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('jugadores/', views.listar_jugadores, name='listar_jugadores'),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador'),
    # ... (Añade las URLs para editar y eliminar)
]

from .views import (
    JugadorListAPIView, EquipoListAPIView, TorneoListAPIView, PartidoListAPIView,
    JugadorDetailAPIView, EquipoDetailAPIView, PaisDetailAPIView
)


urlpatterns += [
    path('api/jugadores/', JugadorListAPIView.as_view(), name='api_jugadores_list'), # [cite: 66]
    path('api/jugadores/<int:pk>/', JugadorDetailAPIView.as_view(), name='api_jugadores_detail'), # [cite: 74]
    path('api/equipos/', EquipoListAPIView.as_view(), name='api_equipos_list'), # [cite: 67]
    path('api/equipos/<int:pk>/', EquipoDetailAPIView.as_view(), name='api_equipos_detail'), # [cite: 75]
    path('api/torneos/', TorneoListAPIView.as_view(), name='api_torneos_list'), # [cite: 70]
    path('api/partidos/', PartidoListAPIView.as_view(), name='api_partidos_list'), # [cite: 71]
    path('api/paises/<int:pk>/', PaisDetailAPIView.as_view(), name='api_paises_detail'), # [cite: 72]
]