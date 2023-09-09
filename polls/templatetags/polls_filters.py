from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiply the arg to the value."""
    return float(value) * float(arg)


@register.filter
def div(value, arg):
    """Divide the value by the arg."""
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0
