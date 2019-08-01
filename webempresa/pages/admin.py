from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','order') #un lista desplaegable que muestra el campo título y el campo de ordenacio order

admin.site.register(Page,PageAdmin)    
