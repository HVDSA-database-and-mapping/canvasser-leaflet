from django.contrib.gis import admin
from .models import CensusTract, CongressionalDistrict, County, Parcel 

admin.site.register(CensusTract, admin.OSMGeoAdmin)
admin.site.register(CongressionalDistrict, admin.OSMGeoAdmin)
admin.site.register(County, admin.OSMGeoAdmin)
admin.site.register(Parcel, admin.OSMGeoAdmin)

