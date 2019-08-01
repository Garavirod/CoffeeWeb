from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    list_display = ('title','author','published','post_categories')
    ordering = ('author','published') #Ordenamos el campo autor seguidamente ordena el campo published
    #Del autor le decimos con las dos barras bajas que busque el usuario
    #Del modelo categoruas buscamos el nombre con las dos guiones bajos
    search_fields = ('title','content','author__username','categories__name',)
    date_hierarchy = 'published'
    #PAsmaos campos para que los filtre.
    list_filter = ('categories__name','author__username')

    # Creamos nuestros propios campos
    # el obj es que cada obj se estara ejecutando la funcipon
    # Esta función se coloca en la tupla del list_display
    def post_categories(self,obj):
        # Juntamos en forma de una lista sacando el nombre de cada categoria
        # Nombre de todas la categorias separadas por comas
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    # Renombra,os el encabezado del nuevo campo CATEGORIAS
    # Tambien se puede insertar HTML, verifaicar docmuennascion en los recursos
    post_categories.short_description = "Categorias"
admin.site.register(Category,CategoryAdmin)        
admin.site.register(Post,PostAdmin)        
