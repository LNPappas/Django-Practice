from django import templatetags, template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    '''
    cuts all values of 'arg' from string
    '''
    return value.replace(arg,'')