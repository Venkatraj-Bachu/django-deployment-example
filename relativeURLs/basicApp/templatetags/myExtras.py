from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts all instances of arg in values
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
