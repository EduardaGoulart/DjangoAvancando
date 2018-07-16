from django import template

register = template.Library()


@register.simple_tag
def footer_message():
    return 'Desenvolvimento Django 2.0.2'


@register.filter
def arredonda(value, casas):
    return round(value,casas)