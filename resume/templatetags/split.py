from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter(name='get_range')
def get_range(value):
    return range(1, value+1, 1)


@register.filter(name='join_var')
def join_var(value, key):
    k = str(key)
    return k.join(value)
