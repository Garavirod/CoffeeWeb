from django.contrib import admin
from .models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    #We create countryside of only reading
    readonly_fields = ('created','updated')

#We register the model and its configuration
admin.site.register(Service,ServiceAdmin)    