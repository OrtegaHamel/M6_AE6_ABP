# M6_AE6_ABP-Ejercicio individual
Por Álvaro Ortega Hamel

##  Instalación y configuración

1. Clonar el repositorio
   ```bash
   git clone https://github.com/TU_USUARIO/plataforma_gestion_eventos.git
   cd plataforma_gestion_eventos
2. Crear y activar entorno virtual
```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
source myenv/bin/activate # Linux/Mac
```

3. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Crear superusuario 
```bash
python manage.py createsuperuser
```
5. Ejecutar servidor
```bash
python manage.py runserver
```
Accede en: http://127.0.0.1:8000

## Funcionalidades

- **Autenticación de usuarios**:
  Inicio y cierre de sesión con redirecciones personalizadas.

- **Gestión de productos**:
  - **Ver productos**: Accesible para usuarios con permiso `view_producto`.
  - **Agregar productos**: Solo usuarios con permiso `add_producto` pueden guardar nuevos productos.
  - **Eliminar productos**: Solo usuarios con permiso `delete_producto` pueden eliminar productos.

- **Manejo de acceso denegado**:
  Si un usuario intenta acceder a una funcionalidad sin permisos, es redirigido a una página de acceso denegado.

- **Interfaz intuitiva**:
  Botones y mensajes claros para interactuar con el sistema.


## Estructura del proyecto

M6_AE6_ABP/
│
├── gestion_productos/          # Proyecto principal
│   ├── settings.py              # Configuraciones
│   ├── urls.py                  # URLs del proyecto
│   └── views.py                 # Vistas globales
│
├── productos/                   # Aplicación de productos
│   ├── admin.py                 # Configuración del admin
│   ├── forms.py                 # Formularios
│   ├── models.py                # Modelos
│   ├── urls.py                  # URLs de la app
│   └── views.py                 # Vistas de productos
│
├── templates/                   # Plantillas
│   ├── base.html                # Plantilla base
│   ├── home.html                # Página de inicio
│   ├── productos/               # Plantillas de productos
│   │   ├── lista_productos.html
│   │   └── confirmar_eliminar.html
│   └── registration/            # Plantillas de autenticación
│       ├── denegado.html
│       └── login.html
│
└── manage.py                    # Script de gestión de Django



## Usuarios de prueba
Se incluyen 3 usuarios de ejemplo. 2 creados vía shell y 1 en la Página Administrativa de Django:

**Administrador**  
usuario: `administrador`  
clave: `contraseña123`  

**Usuario**  
usuario: `usuario_normal`  
clave: `contraseña123`  

**Gestor**  
usuario: `gestor1`  
clave: `contrasena123`