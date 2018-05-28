from django.contrib.gis import admin
from .models import *

admin.site.register(Canvas)
admin.site.register(Canvasser)
admin.site.register(CanvasArea, admin.OSMGeoAdmin)
admin.site.register(Turf, admin.OSMGeoAdmin)
admin.site.register(Campaign)
