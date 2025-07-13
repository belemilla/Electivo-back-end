Backend: Registro de Fútbol ⚽

Este proyecto es un backend desarrollado en Django y Django REST Framework para la administración de una base de datos de fútbol. El sistema permite gestionar jugadores, equipos, torneos y partidos. Además, expone toda la información a través de una API RESTful, preparada para ser consumida por un frontend externo.

Características Principales

Gestión de Datos: CRUD completo para Jugadores y Equipos, implementado con Vistas Basadas en Funciones (FBV).

API REST: Endpoints para consultar listas y detalles de jugadores, equipos, torneos, partidos y países.

Soporte Multimedia: Capacidad para subir y mostrar imágenes para las fotos de los jugadores y los escudos de los equipos.

Base de Datos Relacional: Diseño de base de datos coherente con datos de prueba precargados.

Instalación y Ejecución Local
Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

Clonar el Repositorio

Bash

git clone [https://github.com/belemilla/Electivo-back-end/tree/main/evaluacion_final_backend]
cd [evaluacion_final_backend]
Crear y Activar Entorno Virtual

Bash

# Crear el entorno

python -m venv venv

# Activar en Windows

venv\Scripts\activate

# Activar en macOS/Linux

source venv/bin/activate
Instalar Dependencias
Este proyecto requiere las dependencias listadas en requirements.txt.

Bash

pip install -r requirements.txt
Aplicar Migraciones
Para crear las tablas en la base de datos, ejecuta:

Bash

python manage.py migrate
Ejecutar el Servidor

Bash

python manage.py runserver
El backend estará disponible en http://127.0.0.1:8000/admin.

Cómo Probar la Aplicación
Puedes interactuar con el backend a través del panel de administrador, las vistas del CRUD o los endpoints de la API.

Panel de Administrador
Accede a http://127.0.0.1:8000/admin/. La base de datos ya contiene un superusuario y datos de prueba.

Vistas del CRUD
Listar y gestionar jugadores: http://127.0.0.1:8000/jugadores/

Listar y gestionar equipos: http://127.0.0.1:8000/equipos/

Endpoints de la API REST

Lista de Jugadores: GET /api/jugadores/

Detalle de Jugador: GET /api/jugadores/<id>/

Lista de Equipos con sus jugadores: GET /api/equipos/

Detalle de Equipo con sus jugadores: GET /api/equipos/<id>/

Lista de Torneos con equipos y cantidad de jugadores: GET /api/torneos/

Lista de Partidos: GET /api/partidos/

Detalle de País con sus equipos, jugadores y torneos: GET /api/paises/<id>/
