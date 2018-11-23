from django.contrib import admin
from .models import (ActividadesAgropecuarias, CursoDeAguaHid,
                     EspejoDeAguaHid, EditableModel)
from leaflet.admin import LeafletGeoAdmin


@admin.register(ActividadesAgropecuarias)
class ActividadesAgropecuariasAdmin(LeafletGeoAdmin):

    list_display = ('nombre', 'escala', 'geom')


@admin.register(CursoDeAguaHid)
class CursoDeAguaHidAdmin(LeafletGeoAdmin):

    list_display = ('nombre', 'escala', 'geom')


@admin.register(EspejoDeAguaHid)
class EspejoDeAguaHidAdmin(LeafletGeoAdmin):

    list_display = ('nombre', 'escala', 'geom')


@admin.register(EditableModel)
class EditableModelAdmin(LeafletGeoAdmin):

    list_display = ('campo1', 'campo2', 'geom')
