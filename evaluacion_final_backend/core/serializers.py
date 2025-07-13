# core/serializers.py

from rest_framework import serializers
from .models import Pais, Equipo, Jugador, Torneo, Partido, EquipoTorneo

# --- Serializers Básicos ---
# Estos serializers representan un modelo individual.

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre']

class JugadorSerializer(serializers.ModelSerializer):
    # Muestra el nombre del país y el equipo en lugar de solo sus IDs para mayor claridad.
    pais = serializers.StringRelatedField()
    equipo = serializers.StringRelatedField()
    
    class Meta:
        model = Jugador
        fields = ['id', 'nombre', 'edad', 'posicion', 'pais', 'equipo', 'foto']

class PartidoSerializer(serializers.ModelSerializer):
    # Muestra los nombres de los equipos y torneo.
    equipo_local = serializers.StringRelatedField()
    equipo_visitante = serializers.StringRelatedField()
    torneo = serializers.StringRelatedField()

    class Meta:
        model = Partido
        fields = ['id', 'fecha', 'equipo_local', 'equipo_visitante', 'torneo', 'goles_local', 'goles_visitante']

# --- Serializers con Anidación y Lógica Compleja ---

class EquipoSerializer(serializers.ModelSerializer):
    """
    Serializa un Equipo e incluye una lista anidada de sus jugadores.
    """
    # Usamos el JugadorSerializer para anidar la información completa de los jugadores.
    # 'jugadores' es el 'related_name' que definimos en el ForeignKey del modelo Jugador.
    jugadores = JugadorSerializer(many=True, read_only=True)
    pais = serializers.StringRelatedField()

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'pais', 'entrenador', 'escudo', 'jugadores']

class TorneoSerializer(serializers.ModelSerializer):
    """
    Serializa un Torneo e incluye los equipos participantes y la cantidad de jugadores por equipo.
    """
    # Este campo personalizado calculará y devolverá los datos de los equipos y su cantidad de jugadores.
    equipos_participantes = serializers.SerializerMethodField()
    pais = serializers.StringRelatedField()
    
    class Meta:
        model = Torneo
        # Excluimos el campo 'equipos' original para usar nuestro campo personalizado.
        fields = ['id', 'nombre', 'pais', 'equipos_participantes']

    def get_equipos_participantes(self, obj):
        """
        Método para obtener los equipos y contar sus jugadores.
        Este método cumple el requisito de la API de torneos.
        """
        # obj es la instancia del Torneo que se está serializando.
        equipos = obj.equipos.all()
        resultado = []
        for equipo in equipos:
            resultado.append({
                'nombre_equipo': equipo.nombre,
                'cantidad_jugadores': equipo.jugadores.count() # Contamos los jugadores del equipo.
            })
        return resultado


class PaisDetailSerializer(serializers.ModelSerializer):
    """
    Serializa un País con todos sus datos relacionados: equipos, jugadores y torneos.
    [cite_start]Este serializer cumple con el requisito para el endpoint /api/paises/<id>/. [cite: 72]
    """
    # 1. Anidar Equipos: Relación directa a través del ForeignKey en el modelo Equipo.
    # Usamos el EquipoSerializer para que cada equipo venga con su lista de jugadores.
    equipos = EquipoSerializer(many=True, read_only=True, source='equipo_set')

    # 2. Anidar Torneos: Relación directa a través del ForeignKey en el modelo Torneo.
    # Usamos StringRelatedField para una representación simple y evitar anidación excesiva.
    torneos = serializers.StringRelatedField(many=True, read_only=True, source='torneo_set')

    # 3. Anidar Jugadores: No hay relación directa. Usamos un SerializerMethodField.
    jugadores = serializers.SerializerMethodField()

    class Meta:
        model = Pais
        fields = ['id', 'nombre', 'equipos', 'torneos', 'jugadores']

    def get_jugadores(self, obj):
        """
        Este método recolecta todos los jugadores que pertenecen a los equipos de este país.
        - obj es la instancia del Pais.
        """
        # Obtenemos todos los jugadores cuyo equipo pertenece al país (obj).
        jugadores_del_pais = Jugador.objects.filter(equipo__pais=obj)
        # Usamos el JugadorSerializer para convertir los objetos Jugador a formato JSON.
        return JugadorSerializer(jugadores_del_pais, many=True).data