import datetime

from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(takes_context=True)
def current_time_context(context, format_string):
    return datetime.datetime.now().strftime(format_string)