from django import template

register = template.Library()

@register.filter
def filesize(value):
    if value < 1024:
        return f"{value} B"
    elif value < 1024**2:
        return f"{value / 1024:.2f} KB"
    elif value < 1024**3:
        return f"{value / 1024**2:.2f} MB"
    else:
        return f"{value / 1024**3:.2f} GB"