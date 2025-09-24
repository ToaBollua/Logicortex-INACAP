# Logicortex

Plataforma de Retos Lógicos y Matemáticos.

## Puesta en marcha

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### Prerrequisitos

- Python 3.8 o superior
- pip (manejador de paquetes de Python)

### Instalación

1.  **Clona el repositorio (si aún no lo has hecho):**
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
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución

1.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

2.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

3.  Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.