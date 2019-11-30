from django import template

register = template.Library()

@register.simple_tag
def my_tag(format_string):
    return "HOLA MUNDO: {}".format(format_string)
