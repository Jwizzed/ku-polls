from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value, arg):
    """Multiply the value by the arg."""
    return float(value) * float(arg)


@register.filter
def max_votes(question):
    return question.choice_set.all().order_by("-votes").first().votes
