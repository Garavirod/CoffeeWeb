from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User #Contiene todos los usuarios registradps e el panel de adminstrador

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de acutualización")

    class Meta:
        verbose_name="Categoría"
        verbose_name_plural="Categorías"
        ordering = ['-created']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name="Título")
    content = models.TextField(verbose_name="Contendio")
    published = models.DateTimeField(verbose_name="Fecha de publicación",default=now)#actual date and hour
    imgae = models.ImageField(verbose_name="Imagen", upload_to="blog",null=True,blank=True)
    #Creamos una clave foranea que relaciona una entrada con un usuario revisrado del panel de administración
    author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE) #Actualiza en casacada cada eliminación
    #el related name es un accesor en una relación, es decir puedo acceder a todos los relacionados con él a tra ves de ese "get_posts"
    categories = models.ManyToManyField(Category,verbose_name="Categorias", related_name="get_posts")        
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de acutualización")

    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering = ['-created']
    
    def __str__(self):
        return self.title
