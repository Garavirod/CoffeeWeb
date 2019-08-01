from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):    
    title= models.CharField(verbose_name="Título",max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0) #Entero que no pcia mucho espacio
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de acutualización")

    class Meta:
        verbose_name="página"
        verbose_name_plural="páginas"
        ordering = ['order','title'] #ordenados por el campo name de la linea 6
    
    def __str__(self):
        return self.title