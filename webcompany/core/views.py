from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("home")

def about(request):
    return HttpResponse("about")

def services(request):
    return HttpResponse("services")

def store(request):
    return HttpResponse("store")

def contact(request):
    return HttpResponse("contact")

def blog(request):
    return HttpResponse("Blog")

def sample(request):
    return HttpResponse("Sample")    