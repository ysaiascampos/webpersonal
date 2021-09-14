from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to="proyects")
    link = models.URLField(verbose_name = "Direccion Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title