from django import template
from files.models import PetFile

register = template.Library()


@register.simple_tag
def attr_from_petFile(pk, attr):
    obj = getattr(PetFile.objects.get(pk=int(pk)), attr)
    return obj