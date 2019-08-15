"""AO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
# import cars.views
# from django.conf import settings
# from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
import cars.views
from django.conf import settings
from django.conf.urls.static import static

# User to simple direct to robots.txt
from django.views.generic import TemplateView

# Sitemaps imports
from cars.sitemaps import StaticViewsSitemap_Daily, StaticViewsSitemap_Weekly, CarDetailsSitemap
from django.contrib.sitemaps.views import sitemap

# For favicon only
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView


# Register classes of sitemaps.py
sitemaps = {
    'static_daily': StaticViewsSitemap_Daily,
    'static_weekly': StaticViewsSitemap_Weekly,
    'carDetails': CarDetailsSitemap,
}




urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^', cars.views.index_page, name='index_page'),
    path('admin/', admin.site.urls, ),
    path('', cars.views.index_page, name='index_page'),
    path('automobiliai-visi/', cars.views.automobiliaiVisi_page, name='automobiliaiVisi_page'),
    path('lizingo-informacija/', cars.views.lizingoInformacija_page, name='lizingoInformacija_page'),
    path('susisiekti-kontaktai/', cars.views.kontaktai_page, name='kontaktai_page'),

    # Setting path for detailed cars page using car_id variable
    path('cars/<int:car_id>', cars.views.detailsOfCar, name="automobilioInfo_page"),

    #robots.txt file
    path('robots.txt', TemplateView.as_view(template_name="cars/robots.txt", content_type="text/plain"), name="robots_file"),

    #Sitemmap path
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
