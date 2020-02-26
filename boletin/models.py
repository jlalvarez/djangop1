from django.db import models

# Create your models here.
class usuarios(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self): # toString del Objeto
        cadena=self.nombre+" ("+self.email+")."
        return cadena

