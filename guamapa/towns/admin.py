from django.contrib.gis import admin
from .models import Business

admin.site.register(Business, admin.GeoModelAdmin)
