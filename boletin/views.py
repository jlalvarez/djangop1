from django.shortcuts import render

from .models import Usuario

# Create your views here.

from .forms import SingupForm

def inicio(request):
    form = SingupForm(request.POST or None)
    print(dir(form))
    if form.is_valid():
        form_data = form.cleaned_data
        nombreForm = form_data.get("nombre")
        emailForm = form_data.get("email")
        u = Usuario.objects.create(nombre=nombreForm, email=emailForm)
        
        # Otra opción
        # u = Usuario()
        # u.nombre = nombreForm
        # u.email = emailForm
        # u.save()
        
        
    contexto = {
        "form": form,
    }
    return render(request, "inicio.html", contexto)
