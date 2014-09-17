#!env/bin/python
# -*- coding: utf-8 -*-
from django import template
from contenidos.models import Diapositiva, Novedad

register = template.Library()


def next(value, arg):
    """ Devuelve el próximo elemento de la lista """
    try:
        return value[int(arg) + 1]
    except:
        return {'slug': 'novedades'}

register.filter('next', next)

@register.inclusion_tag('contenidos/diapositivas.html')
def diapositivas():

    object_list = Diapositiva.objects.all()

    return {
        'object_list': object_list,
    }

@register.inclusion_tag('contenidos/novedades.html')
def novedades():

    object_list = Novedad.objects.all()

    return {
        'object_list': object_list,
    }