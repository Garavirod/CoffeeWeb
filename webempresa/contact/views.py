from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    #instanceamos un formulario para poderlo enviar al template en un diccionario de contexto
    contact_form = ContactForm() #Plantilla vacáa
    if request.method == "POST":
        #Incluye los campos del formulario que se han enviado
        #Se rellenan los campos automaticamente 
        contact_form = ContactForm(data=request.POST) #si se han mando rellenarla con la información
        if contact_form.is_valid():
            name = request.POST.get('name','') #De no haber ninguno que nos devuelva una cadena vacía
            email = request.POST.get('email','') #De no haber ninguno que nos devuelva una cadena vacía
            content = request.POST.get('content','') #De no haber ninguno que nos devuelva una cadena vacía
            #Envíamos correro 
            email =EmailMessage(
                    "La cafetiera: Nuevo mensaje de contacto",
                    "De {} <{}>\n\n{}".format(name,email,content),
                    "no-contestar@inbox.mailtrap.io",
                    ["rodrigogarciaavila26@gmail.com"],
                    reply_to=[email] #persona qeu se pone en cntacto, correo de usaurio destinatario                    
            )
            try:                
                email.send()
                #Todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")

            except:
                #Algo no ha ido bbien, redireccionamos a fail
                return redirect(reverse('contact')+"?fail")

    return render(request,"contact/contact.html",{'form':contact_form})    