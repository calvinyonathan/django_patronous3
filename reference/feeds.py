from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Reference

class LatestReferencesFeed(Feed):
    link = reverse_lazy('reference:reference_list')
    

    def items(self):
        return Reference.objects.all()[:5]
        
    def item_title(self,item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
