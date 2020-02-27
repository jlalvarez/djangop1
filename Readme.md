
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
    list_display = ["__str__", "nombre", "emai", "timestamp"]
    list_filter = ["timestamp"]
    list_editable = ["email"]
    search_fields = ["nombre", "email"]
    class Meta:
        model = Usuario


admin.site.register(Usuario, AdminUsuario)



## Crear una vista

En el fichero views.py incluir:

def inicio(request):
    return render(request, "vista.html", contexto)


## Crear template
En el fiichero nombre_proy/settings.py se incluyen las rutas a los templates en la sección DIRS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

Para crear una ruta usamos: os.path.join(BASE_DIR, ...)

Por ejemplo, incluimos:

TEMPLATES = [
    {
    ,,,
        'DIRS': [os.path.join(BASE_DIR, "templates")],
    ...
]

En la ruta será necesario crear las vistas
 ../templates/vista.html


## Asociar una URL a una acción

En el fichero nombre_proy/urls.py añadir:

from boletin import views

urlpatterns = [
    ...
    path('', views.inicio, name='home')
]




## Crear Formularios

En la app crear un fichero form.py y añadir:

from django import forms

class SingupForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)


### Añadir a una vista

En views.py, importar el formulario e incluir en la acción correspodiente:

```python
from .forms import SingupForm

def inicio(request):
    form = SingupForm()
    contexto = {
        "form": form,
    }
    return render(request, "vista.html", contexto)
```

En la plantilla renderizar con {{ }}, por ejemplo el vista.html

<h1>Alta usuario</h1>

<form method="POST" action="">{% csrf_token %}
{{ form.as_p }}
<input type="submit" value="Registrar" />
</form>


... continuará ...