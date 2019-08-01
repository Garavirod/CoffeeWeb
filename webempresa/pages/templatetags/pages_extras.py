from django import template #se registra en ña libreria de django
from pages.models import Page # Importamos nuestro modelos de paginas


register = template.Library() #Registrmoa el emplate que acabsmo de crear en la libreria de templates 
#Implemantamos un decorador 
@register.simple_tag
def get_page_list():
    pages =Page.objects.all() #Recuperamos todas la páginas
    return pages #Lo devolvemos en froma de template tag