from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home']

    def location(self, obj):
        return reverse(obj)