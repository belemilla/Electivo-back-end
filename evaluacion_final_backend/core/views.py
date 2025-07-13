# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Jugador, Pais, Partido, Torneo
from .forms import EquipoForm, JugadorForm

# ------------------- CRUD para Equipo -------------------

def listar_equipos(request):
    """Muestra una lista de todos los equipos."""
    equipos = Equipo.objects.all()
    return render(request, 'core/equipo/listar.html', {'equipos': equipos})

def detalle_equipo(request, pk):
    """Muestra los detalles de un equipo específico."""
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'core/equipo/detalle.html', {'equipo': equipo})

def crear_equipo(request):
    """Crea un nuevo equipo usando un formulario."""
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_equipos')
    else:
        form = EquipoForm()
    return render(request, 'core/equipo/formulario.html', {'form': form, 'title': 'Crear Equipo'})

def editar_equipo(request, pk):
    """Edita un equipo existente."""
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('listar_equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'core/equipo/formulario.html', {'form': form, 'title': 'Editar Equipo'})

def eliminar_equipo(request, pk):
    """Elimina un equipo existente."""
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        equipo.delete()
        return redirect('listar_equipos')
    return render(request, 'core/equipo/confirmar_eliminar.html', {'objeto': equipo})


# ------------------- CRUD para Jugador -------------------

def listar_jugadores(request):
    """Muestra una lista de todos los jugadores."""
    jugadores = Jugador.objects.all()
    return render(request, 'core/jugador/listar.html', {'jugadores': jugadores})

def detalle_jugador(request, pk):
    """Muestra los detalles de un jugador específico."""
    jugador = get_object_or_404(Jugador, pk=pk)
    return render(request, 'core/jugador/detalle.html', {'jugador': jugador})

def crear_jugador(request):
    """Crea un nuevo jugador usando un formulario."""
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_jugadores')
    else:
        form = JugadorForm()
    return render(request, 'core/jugador/formulario.html', {'form': form, 'title': 'Crear Jugador'})

def editar_jugador(request, pk):
    """Edita un jugador existente."""
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('listar_jugadores')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'core/jugador/formulario.html', {'form': form, 'title': 'Editar Jugador'})

def eliminar_jugador(request, pk):
    """Elimina un jugador existente."""
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        jugador.delete()
        return redirect('listar_jugadores')
    return render(request, 'core/jugador/confirmar_eliminar.html', {'objeto': jugador})

# core/views.py (añadir al final)

from rest_framework import generics
from .serializers import (
    JugadorSerializer, EquipoSerializer, TorneoSerializer,
    PartidoSerializer, PaisDetailSerializer
)

# Endpoints de Lista [cite: 65]
class JugadorListAPIView(generics.ListAPIView):
    queryset = Jugador.objects.all() # [cite: 66, 68]
    serializer_class = JugadorSerializer

class EquipoListAPIView(generics.ListAPIView):
    queryset = Equipo.objects.all() # [cite: 67, 69]
    serializer_class = EquipoSerializer

class TorneoListAPIView(generics.ListAPIView):
    queryset = Torneo.objects.all() # [cite: 70]
    serializer_class = TorneoSerializer
    
class PartidoListAPIView(generics.ListAPIView):
    queryset = Partido.objects.all() # [cite: 71]
    serializer_class = PartidoSerializer

# Endpoints de Detalle [cite: 73]
class JugadorDetailAPIView(generics.RetrieveAPIView):
    queryset = Jugador.objects.all() # [cite: 74]
    serializer_class = JugadorSerializer

class EquipoDetailAPIView(generics.RetrieveAPIView):
    queryset = Equipo.objects.all() # [cite: 75]
    serializer_class = EquipoSerializer

class PaisDetailAPIView(generics.RetrieveAPIView):
    queryset = Pais.objects.all() # [cite: 72]
    serializer_class = PaisDetailSerializer