from django.contrib.gis import admin
from .models import *

admin.site.register(CensusTract, admin.OSMGeoAdmin)
admin.site.register(CongressionalDistrict, admin.OSMGeoAdmin)
admin.site.register(County, admin.OSMGeoAdmin)
admin.site.register(Parcel, admin.OSMGeoAdmin)
admin.site.register(Canvas)
admin.site.register(Canvasser)
admin.site.register(CanvasArea, admin.OSMGeoAdmin)
admin.site.register(Turf, admin.OSMGeoAdmin)
admin.site.register(Campaign)
