from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Programas


def programas(request):
    lista_programas = Programas.objects.all().values()
    template = loader.get_template('lista_programas.html')
    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_programa(request, programa_id):
    programa = Programas.objects.get(id=programa_id)
    template = loader.get_template('detalle_programa.html')
    context = {
        'programa': programa,
    }
    return HttpResponse(template.render(context, request))
