# Logicortex

Plataforma de Retos Lógicos y Matemáticos.

## Descripción

Logicortex es una aplicación web desarrollada con Django que permite a los usuarios registrarse, resolver retos de lógica y matemática, y acumular puntos según la dificultad de los retos completados.

## Puesta en marcha

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### Prerrequisitos

- Python 3.8 o superior
- pip (manejador de paquetes de Python)

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd Logicortex
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    *En Windows, usa `venv\Scripts\activate`*

3.  **Instala las dependencias:**
    Las dependencias del proyecto se encuentran en el archivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución

1.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

2.  **Crea un superusuario para acceder al panel de administración:**
    ```bash
    python manage.py createsuperuser
    ```

3.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

4.  Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación. El panel de administración está en `http://127.0.0.1:8000/admin/`.

## Estructura del Proyecto

```
Logicortex/
├── core/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py      # Configuración del panel de administración
│   ├── apps.py
│   ├── models.py     # Modelos de la base de datos (CustomUser, Reto, etc.)
│   ├── tests.py
│   └── views.py
├── logicortex/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py   # Configuración principal del proyecto
│   ├── urls.py
│   └── wsgi.py
├── static/           # Archivos estáticos (CSS, JS, imágenes)
├── venv/             # Entorno virtual (ignorado por git)
├── .gitignore        # Archivos y carpetas ignorados por git
├── db.sqlite3        # Base de datos (ignorada por git)
├── manage.py         # Script de gestión de Django
└── README.md         # Este archivo
```
