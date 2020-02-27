from django.shortcuts import render

# Create your views here.

from .forms import SingupForm

def inicio(request):
    form = SingupForm()
    contexto = {
        "form": form,
    }
    return render(request, "inicio.html", contexto)
