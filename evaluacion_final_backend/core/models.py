
from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100) # [cite: 27]

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100) # [cite: 29]
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE) # [cite: 31]
    entrenador = models.CharField(max_length=100) # [cite: 32]
    escudo = models.ImageField(upload_to='escudos/') # [cite: 33]

    def __str__(self):
        return self.nombre

class Torneo(models.Model):
    nombre = models.CharField(max_length=100) # [cite: 35]
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE) # [cite: 37]
    equipos = models.ManyToManyField(Equipo, through='EquipoTorneo')

    def __str__(self):
        return self.nombre

class EquipoTorneo(models.Model): # Tabla intermedia para la relación ManyToMany [cite: 38, 89]
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE) # [cite: 39]
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE) # [cite: 40]

    class Meta:
        unique_together = ('equipo', 'torneo')

class Jugador(models.Model):
    nombre = models.CharField(max_length=100) # [cite: 42]
    edad = models.IntegerField() # [cite: 44]
    posicion = models.CharField(max_length=50) # [cite: 45]
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE) # [cite: 46]
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores') # [cite: 47]
    foto = models.ImageField(upload_to='fotos_jugadores/') # [cite: 48]

class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

def __str__(self):
        return self.nombre
    
class Partido(models.Model):
    fecha = models.DateField() # [cite: 50]
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local') # [cite: 51]
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante') # [cite: 52]
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE) # [cite: 53]
    goles_local = models.IntegerField() # [cite: 54]
    goles_visitante = models.IntegerField() # [cite: 55]

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"
