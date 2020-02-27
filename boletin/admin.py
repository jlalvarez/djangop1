from django.contrib import admin

# Register your models here.
from .models import Usuario


class AdminUsuario(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "email", "timestamp"]
    list_filter = ["timestamp"]
    list_editable = ["nombre", "email"]
    search_fields = ["nombre", "email"]
    class Meta:
        model = Usuario


admin.site.register(Usuario, AdminUsuario)


