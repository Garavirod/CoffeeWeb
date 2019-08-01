from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html",{'posts':posts})

def category(request,category_id):
    #el 'get' nos permite obtener un único registro filtrado ppor una serie de campos por el parametro    
    # category = Category.objects.get(id=category_id) 
    # Los paraámetros serán el modelo y el identificador de la categoría
    #Buscamos a la inversa todas la entradas que tengan asignada esta categoría
    category = get_object_or_404(Category,id=category_id) #Nos muestra el error 404 según el modelo
    posts = Post.objects.filter(categories=category) #Filatra los datos por categoría
    return render(request,"blog/category.html",{'category':category})