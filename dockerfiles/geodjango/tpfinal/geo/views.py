import json
import re
import ast
from itertools import chain
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from geo.models import *


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def render_html_01(request):
    template_name = 'html_01.html'
    return render(request, template_name)


def render_html_02(request):
    template_name = 'html_02.html'
    return render(request, template_name)


def _snake_to_camel(string):
    return ''.join(x.capitalize() for x in string.split('_'))


@csrf_exempt
def consulta(request):
    """ Recibe en request.body un archivo json
            {
                "model_names": ["salvado_de_obstaculo", "curso_de_agua_hid"],
                "geom": "POINT(123123 12312)"
            }
    """
    data = {}
    if request.method == 'POST':
        try:
            string_data = request.body.decode('utf-8')
            data = ast.literal_eval(string_data)
        except json.JSONDecodeError:
            raise Http404("NO CARGA EL PUTO JSON")

    try:
        model_names = data['model_names']
        geometry = GEOSGeometry(data['geom'], srid=4326)
    except ValueError:
        raise Http404("parse error - invalid geometry")

    querys = [
        globals()[_snake_to_camel(model)].objects.filter(
            geom__intersects=geometry)[:25]
        for model in model_names
    ]
    result = chain.from_iterable(querys)
    result_serialized = serialize('json', result)
    return HttpResponse(result_serialized, content_type='json')


@csrf_exempt
def consulta2(request):
    """ Recibe en request.body un archivo json
            {
                "model_names": ["salvado_de_obstaculo", "curso_de_agua_hid"],
                "geom": "POINT(123123 12312)"
            }
    """
    data = {}
    if request.method == 'POST':
        try:
            string_data = request.body.decode('utf-8')
            data = json.loads(string_data)
        except json.JSONDecodeError:
            raise Http404("NO CARGA EL PUTO JSON")

    try:
        model_names = data['model_names']
        geometry = GEOSGeometry(data['geom'], srid=4326)
    except ValueError:
        raise Http404("parse error - invalid geometry")

    querys = [
        globals()[_snake_to_camel(model)].objects.filter(
            geom__intersects=geometry)[:25]
        for model in model_names
    ]
    result = chain.from_iterable(querys)
    result_serialized = serialize('json', result)
    return HttpResponse(result_serialized, content_type='json')


@csrf_exempt
def agregar_elementos(request):
    """ Recibe un json
            {
                "campo1": "string1",
                "campo2": "string2",
                "geoms": "POINT(123123 12312)"
            }
    """
    data = {}
    if request.method == 'POST':
        try:
            string_data = request.body.decode('utf-8')
            data = ast.literal_eval(string_data)
        except json.JSONDecodeError:
            raise Http404("NO CARGA EL PUTO JSON")

    try:
        geometry = GEOSGeometry(data['geom'], srid=4326)
    except ValueError:
        raise Http404("parse error - invalid geometry")

    new = EditableModel(campo1=data['campo1'],
                        campo2=data['campo2'], geom=geometry)
    new.save()
    return HttpResponse(status=204)


def mostrar_capa_editable(request):
    geometrias = EditableModel.objects.all()
    return HttpResponse(serialize('geojson', geometrias))
