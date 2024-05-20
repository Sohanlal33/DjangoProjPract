import datetime
from django import template

register=template.Library()

#used decorator
@register.simple_tag(name="today")
def grt_date():
    n=datetime.datetime.now()
    return n

@register.filter
def quotes(value):
        s='"'+str(value)+'"'
        return s