# En tu_app/templatetags/base64_filters.py
import base64
from django import template

register = template.Library()

@register.filter
def base64_encode(value):
    return base64.urlsafe_b64encode(value.encode()).decode()
