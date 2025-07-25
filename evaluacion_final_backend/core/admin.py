# core/admin.py

from django.contrib import admin
from .models import Pais, Equipo, Torneo, EquipoTorneo, Jugador, Partido

# Aquí registramos cada uno de los modelos para que aparezcan en el panel de administrador.
admin.site.register(Pais)
admin.site.register(Equipo)
admin.site.register(Torneo)
admin.site.register(EquipoTorneo)
admin.site.register(Jugador)
admin.site.register(Partido)