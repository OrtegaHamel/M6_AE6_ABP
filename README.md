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
3. Instalar dependencias
```bash
Copiar código
pip install -r requirements.txt
```
4. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Crear superusuario 
```bash
python manage.py createsuperuser
```
6. Ejecutar servidor
```bash
python manage.py runserver
```
Accede en: http://127.0.0.1:8000

## Funcionalidades


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