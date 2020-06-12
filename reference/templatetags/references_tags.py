from django import template
from ..models import Reference


register = template.Library()

@register.simple_tag()
def total_references():
    return Reference.objects.count()

@register.inclusion_tag('reference/reference_list/latest_references.html')
def show_latest_references(count=5):
    latest_references = Reference.objects.order_by('-publish')[:count]
    return {'latest_references': latest_references}