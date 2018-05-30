from django import template

register = template.Library()
import datetime

@register.filter(name='fromunix')
def fromunix(value):
    return datetime.datetime.fromtimestamp(int(value))