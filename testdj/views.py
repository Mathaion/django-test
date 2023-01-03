from django.http import HttpResponse
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render

import datetime

def saludo(request):
    nombre = "Oppenheimer"
    return render(request, "plantilla.html", {"nombre_persona":nombre})


def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(documento)

def despedida_html(request):
    documento="""<html><body><h1>Hola a todos!</h1></body></html>"""
    return HttpResponse(documento)

def calcular_edad(request, age, year):
    periodo = year - 2022
    edad_futuro = age+periodo
    documento="""<html><body><h1>En el año %s va a tener %s años</h1></body></html>""" %(year, edad_futuro)
    return HttpResponse(documento)

def salu2(request):
    archivo=open("C:/Users/Usuario/Documents/Matías/Coding/django-test/templates/plantilla.html")
    nombre = "Matías"
    edad = "27"
    planeta = "Saturno"
    fecha = datetime.datetime.now()
    lectura=Template(archivo.read())
    archivo.close()
    assignments=["quantum mechanics", "general relativity", "the second law", "dark matter"]
    ctx = Context({"nombre":nombre, "edad":edad, "planeta":planeta, "fecha":fecha, "year":2022, "cursos":assignments})
    documento = lectura.render(ctx)
    return HttpResponse(documento)

def curso(request):
    fecha = datetime.datetime.now()
    lectura=Template(archivo.read())
    documento = lectura.render(ctx)
    return HttpResponse(documento)

# def home(request):
#    archivo=open("C:/Users/Usuario/Documents/Matías/Coding/django-test/templates/home.html")
#    lectura=Template(archivo.read())
#    archivo.close()
#    ctx = Context({})
#    documento = lectura.render(ctx)
#    return HttpResponse(documento) 