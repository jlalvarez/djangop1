from django.contrib import admin

# Register your models here.
from .models import Usuario


class AdminUsuario(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "timestamp"]
    class Meta:
        model = Usuario


admin.site.register(Usuario, AdminUsuario)


