from django.contrib.gis import admin
from .models import *

admin.site.register(Canvass)
admin.site.register(Canvasser)
admin.site.register(CanvassArea, admin.OSMGeoAdmin)
admin.site.register(Turf, admin.OSMGeoAdmin)
admin.site.register(Campaign)
