from django.http import HttpResponse
from django.shortcuts import render
from .models import Fam
from django.template import Template, Context, loader

# Create your views here.
def datos(self):
    fam = Fam( nombre = "Nicolas" , numero = 7 , fechaDeNac = '2001-1-27')
    fam.save()
    texto = f"Nombre: {fam.nombre}  Numero:{fam.numero} Cumple:{fam.fechaDeNac}"
    
    return HttpResponse(texto)

def datos1(self):
    fam = Fam( nombre = ("Nicolas" , "Juan" , "Martin") , numero = (7 , 8 , 9) , fechaDeNac = ('2001-1-27' , '2000-2-28' , '1999-3-29'))
    fam.save()
    diccionario = {"nombre":fam.nombre , "numero": fam.numero , "fecha" : fam.fechaDeNac}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
    
def datos2(request):
    datos_list = Fam.objects.all()
    diccionario = {'datos_list':datos_list}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento) 
    