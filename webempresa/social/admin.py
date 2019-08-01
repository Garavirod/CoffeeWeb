from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    #Extendemos la funcion en teipo de ejecucion de solo poder leer los datos solamente
    def get_readonly_fields(self, request, obj=None):
        #PReguntamos con request si dentro del grupo personal existe ese user
        if request.user.groups.filter(name="Personal").exists():
            #Para mostrara todos los campo poner 
            # return ('created','updated','key','name')
            return ('key','name')
        else:
            return ('created','updated')

admin.site.register(Link,LinkAdmin)    
