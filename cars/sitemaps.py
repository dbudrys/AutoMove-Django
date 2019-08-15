from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import CarDetails

# Only Static Views
class StaticViewsSitemap_Daily(Sitemap):

    priority = 0.8
    changefreq = 'daily'

    # Add all of the url page names of static files
    def items(self):
        return ['index_page', 'automobiliaiVisi_page',]

    def location(self, item):
        return reverse(item)
        
class StaticViewsSitemap_Weekly(Sitemap):

    priority = 0.5
    changefreq = 'weekly'

    # Add all of the url page names of static files
    def items(self):
        return ['lizingoInformacija_page', 'kontaktai_page',]

    
    def location(self, item):
        return reverse(item)



# Induvidual car files 
class CarDetailsSitemap(Sitemap):
    priority = 0.4
    changefreq = 'weekly'

    # Last modification date
    def lastmod(self, obj):
        return obj.skelbimasSukurtas

    def items(self):
        return CarDetails.objects.all()