from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
    return HttpResponse("Hola mundo")


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
    archivo=open("C:/Users/usuario/Documents/Cursos/Python Codo a Codo/django/testdj/templates/plantilla.html")
    nombre = "Matías"
    edad = "27"
    planeta = "Saturno"
    fecha = datetime.datetime.now()
    lectura=Template(archivo.read())
    archivo.close()
    ctx = Context({"nombre":nombre, "edad":edad, "planeta":planeta, "fecha":fecha, "year":2022})
    documento = lectura.render(ctx)
    return HttpResponse(documento)
