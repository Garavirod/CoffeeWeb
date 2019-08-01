from django.urls import path
from . import views 
urlpatterns = [
    path('',views.blog,name="blog"),
    #Tomara lo que halla entre  '< >' y lo pasará a la vista category como parámetro
    path('category/<int:category_id>/',views.category, name="category"),  
]