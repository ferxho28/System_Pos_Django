# SIFS - Sistema de Punto de Venta

SIFS es una aplicación de sistema de punto de venta (POS) desarrollada en Django. Esta aplicación permite gestionar ventas, productos, categorías, clientes y más, ofreciendo una interfaz amigable y funcional para el manejo eficiente de un negocio.

## Características

- **Dashboard**: Resumen de ventas por mes, ganancias por año, y registros de productos y categorías.
- **Gestión de Productos y Categorías**: Crear, editar, eliminar y exportar productos y categorías en formatos CSV, PDF o Excel.
- **Gestión de Clientes y Ventas**: Funcionalidades similares para clientes y ventas.
- **Frontend**: Construido con Bootstrap 5, CSS y SCSS para una experiencia de usuario moderna y responsiva.

## Requisitos

- Python 3.9 o superior
- Django 4.1.5
- SQLite (incluido por defecto en Django)
- Docker (opcional, para despliegue con contenedores)

## Instalación

### Configuración del Entorno

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/sifs.git
   cd sifs
   ```

2. **Crear un Entorno Virtual:**
   ```bash
   python3 -m venv nombre_del_entorno
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar Dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

   El archivo `requirements.txt` debe incluir las siguientes dependencias:

   ```plaintext
   asgiref==3.8.1
   attrs==23.2.0
   Brotli==1.1.0
   certifi==2024.6.2
   cffi==1.16.0
   cssselect2==0.7.0
   Django==4.1.5
   fonttools==4.53.0
   h11==0.14.0
   html5lib==1.1
   idna==3.7
   iniconfig==2.0.0
   outcome==1.3.0.post0
   packaging==24.1
   pillow==10.3.0
   pluggy==1.5.0
   pycparser==2.22
   pydyf==0.10.0
   pyphen==0.15.0
   PySocks==1.7.1
   pytest==8.2.2
   pytest-django==4.8.0
   selenium==4.22.0
   six==1.16.0
   sniffio==1.3.1
   sortedcontainers==2.4.0
   sqlparse==0.5.0
   tinycss2==1.3.0
   trio==0.25.1
   trio-websocket==0.11.1
   typing_extensions==4.12.2
   urllib3==2.2.2
   weasyprint==62.1
   webencodings==0.5.1
   websocket-client==1.8.0
   wsproto==1.2.0
   zopfli==0.2.3
   ```

### Configuración de la Base de Datos

1. **Aplicar Migraciones:**
   ```bash
   python manage.py migrate
   ```

2. **Crear un Superusuario (opcional, para acceder al panel de administración):**
   ```bash
   python manage.py createsuperuser
   ```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Accede a la aplicación en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Uso

- **Dashboard**: Ver el resumen de ventas y productos.
- **Productos y Categorías**: Añadir, editar y eliminar productos y categorías desde el dashboard.
- **Clientes y Ventas**: Gestionar clientes y registrar ventas.

## Despliegue con Docker (Opcional)

1. **Construir la Imagen de Docker:**
   ```bash
   docker-compose build
   ```

2. **Iniciar los Contenedores:**
   ```bash
   docker-compose up
   ```

3. **Acceder a la Aplicación:**
   Abre [http://localhost:8000](http://localhost:8000) en tu navegador.


