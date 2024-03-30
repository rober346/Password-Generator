from django.shortcuts import render
# from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    # Genera la contraseña segun el numero de caracteres que se indique

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    
    # Puede obtener la propiedad de longitud del menu y del navegador:
    length = int(request.GET.get('length'))

    # Añadiendo los posibles caracteres adicionales para la contraseña: 
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('-_+!@#$%&*()'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})
