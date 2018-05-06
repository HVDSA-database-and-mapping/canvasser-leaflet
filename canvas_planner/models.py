# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class CensusTract(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    geoid = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=7, blank=True, null=True)
    namelsad = models.CharField(max_length=20, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    awater = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'census_tract'


class CongressionalDistrict(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    cd115fp = models.CharField(max_length=2, blank=True, null=True)
    affgeoid = models.CharField(max_length=13, blank=True, null=True)
    geoid = models.CharField(max_length=4, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    cdsessn = models.CharField(max_length=3, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congressional_district'


class County(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    countyns = models.CharField(max_length=8, blank=True, null=True)
    affgeoid = models.CharField(max_length=14, blank=True, null=True)
    geoid = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county'


class Parcel(models.Model):
    short_pin = models.CharField(max_length=100, blank=True, null=True)
    zoning = models.CharField(max_length=100, blank=True, null=True)
    pre_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pre_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    eq_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tent_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    acreage_of_parent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    assessed_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    building_assessment = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    capped_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cvt_code = models.CharField(max_length=10, blank=True, null=True)
    cvt_description = models.CharField(max_length=40, blank=True, null=True)
    historical_district = models.CharField(max_length=4, blank=True, null=True)
    homestead_taxable = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    homestead_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lastupdate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    legal_description = models.TextField(blank=True, null=True)
    owner_care_of = models.CharField(max_length=100, blank=True, null=True)
    owner_city = models.CharField(max_length=100, blank=True, null=True)
    owner_country = models.CharField(max_length=100, blank=True, null=True)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    owner_name2 = models.CharField(max_length=100, blank=True, null=True)
    owner_state = models.CharField(max_length=2, blank=True, null=True)
    owner_street = models.CharField(max_length=100, blank=True, null=True)
    owner_zip = models.CharField(max_length=20, blank=True, null=True)
    parent_parcel_num = models.CharField(max_length=40, blank=True, null=True)
    pin = models.CharField(max_length=40, blank=True, null=True)
    prop_city = models.CharField(max_length=100, blank=True, null=True)
    prop_class = models.CharField(max_length=10, blank=True, null=True)
    prop_class_description = models.CharField(max_length=100, blank=True, null=True)
    prop_state = models.CharField(max_length=2, blank=True, null=True)
    prop_street = models.CharField(max_length=100, blank=True, null=True)
    prop_street_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    prop_zip = models.CharField(max_length=20, blank=True, null=True)
    school_district = models.CharField(max_length=100, blank=True, null=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    sev = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stated_area = models.CharField(max_length=20, blank=True, null=True)
    status_code = models.CharField(max_length=4, blank=True, null=True)
    status_desc = models.CharField(max_length=20, blank=True, null=True)
    taxable_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    txpyrs_care_of = models.CharField(max_length=100, blank=True, null=True)
    txpyrs_city = models.CharField(max_length=100, blank=True, null=True)
    txpyrs_country = models.CharField(max_length=100, blank=True, null=True)
    txpyrs_name = models.CharField(max_length=100, blank=True, null=True)
    txpyrs_state = models.CharField(max_length=100, blank=True, null=True)
    txpyrs_street_addr = models.CharField(max_length=100, blank=True, null=True)
    txpyrs_zip_code = models.CharField(max_length=20, blank=True, null=True)
    unit_apt_num = models.CharField(max_length=20, blank=True, null=True)
    geometry = models.TextField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)
    lon_centroid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lat_centroid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    county_gid = models.IntegerField(blank=True, null=True)
    cd_gid = models.IntegerField(blank=True, null=True)
    ct_gid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel'
