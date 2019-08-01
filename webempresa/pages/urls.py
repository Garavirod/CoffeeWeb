from django.urls import path
from . import views 
urlpatterns = [    
    #Tomara lo que halla entre  '< >' y lo pasará a la vista category como parámetro
    path('<int:page_id>/<slug:page_slug>',views.page, name="page"),  
]