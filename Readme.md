
## Primeros Pasos

Instalar Python
Instalar pip 
Instalar Django

Podríamos crear un entorno de desarrollo con VirtualEnv

Ver paquetes instalados con $ pip freeze

## Crear proyecto Django
$  django-admin startproject <nombre_proy>

## Iniciar proyecto
$ python manage.py runserver 0:8000

Acceder al proyecto: http://ip-maquina:8080

## Crear un superusuario
$ python manage.py createsuperuser

Acceder al administración:  http://ip-maquina:8080/admin



## Crear App. Un proyecto puede tener varias App
$ python manage.py startapp <nombre_APP>

## Registrar la App en settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'django.contrib.staticfiles',
    'nombre_APP',
]

## Crear un modelo

En el fichero models.py de la app deseada creamos una clase con atributos. Los
tipos de datos: https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

class Usuario(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


## Migraciones 

$ python manage.py makemigrations

$ python manage.py migrate



## Utilizar la consola iteractiva

$ python manage.py shell

Importar modelo a la consola : from boletin.models import Usuario   

Obtener listado de objetos del modelo: usuarios = Usuario.objects.all()

Crear objetos:  u1 = Usuario.objects.create(nombre='Pepe',email='pepe@mail.com')   

## Registrar un modelo

En el fichero admin.py: importamos el modelo y lo registramos

from .models import Usuario

admin.site.register(Usuario)



### Personalizar la interfaz

class AdminUsuario(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "timestamp"]
    class Meta:
        model = Usuario


admin.site.register(Usuario, AdminUsuario)



... continuará ...