from django.shortcuts import render

# Create your views here.

from .forms import SingupForm

def inicio(request):
    form = SingupForm(request.POST or None)
    print(dir(form))
    if form.is_valid():
        form_data = form.cleaned_data
        print(form_data.get("nombre"))
        print(form_data.get("email"))
        
    contexto = {
        "form": form,
    }
    return render(request, "inicio.html", contexto)
