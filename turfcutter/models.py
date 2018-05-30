from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from datetime import date


class Campaign(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=140)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return '/campaign-details/%d/' % self.id


class Canvasser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return '/canvasser-details/%d/' % self.id


class Canvas(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=140)
    date = models.DateField(default=date.today)
    description = models.TextField(blank=True)
    canvassers = models.ManyToManyField(Canvasser)
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return '/canvas-details/%d/' % self.id


class CanvasArea(models.Model):
    canvas = models.OneToOneField(Canvas,
        on_delete=models.CASCADE, primary_key=True)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return '%s Area' % self.canvas.name


class Turf(models.Model):
    canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE)
    canvassers = models.ManyToManyField(Canvasser, blank=True)
    name = models.CharField(max_length=140)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return '%s Turf %s' % (self.canvas.name, self.name)

    def get_absolute_url(self):
        return '/turf-canvas/%d/' % self.id


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
    aland = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    awater = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'census_tract'

    def __str__(self):
        return '%s' % self.name


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

    def __str__(self):
        return 'District %s' % self.cd115fp


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

    def __str__(self):
        return '%s County' % self.name


class Parcel(models.Model):
    short_pin = models.CharField(max_length=100, blank=True, null=True)
    zoning = models.CharField(max_length=100, blank=True, null=True)
    pre_percent = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    pre_value = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    eq_value = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    tent_value = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    acreage_of_parent = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    assessed_value = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    building_assessment = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    capped_value = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    cvt_code = models.CharField(max_length=10, blank=True, null=True)
    cvt_description = models.CharField(max_length=40, blank=True, null=True)
    historical_district = models.CharField(max_length=4, blank=True, null=True)
    homestead_taxable = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    homestead_percent = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    lastupdate = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
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
    prop_class_description = models.CharField(max_length=100,
        blank=True, null=True)
    prop_state = models.CharField(max_length=2, blank=True, null=True)
    prop_street = models.CharField(max_length=100, blank=True, null=True)
    prop_street_num = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    prop_zip = models.CharField(max_length=20, blank=True, null=True)
    school_district = models.CharField(max_length=100, blank=True, null=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    sev = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    stated_area = models.CharField(max_length=20, blank=True, null=True)
    status_code = models.CharField(max_length=4, blank=True, null=True)
    status_desc = models.CharField(max_length=20, blank=True, null=True)
    taxable_value = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
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
    centroid = models.PointField()
    lon_centroid = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    lat_centroid = models.DecimalField(max_digits=65535,
        decimal_places=65535, blank=True, null=True)
    county_gid = models.IntegerField(blank=True, null=True)
    cd_gid = models.IntegerField(blank=True, null=True)
    ct_gid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel'

    def __str__(self):
        return '%s' % self.pin

RESPONSE_CHOICES = (
    (1, u'\U0001F620'),
    (2, u'\U0001F610'),
    (3, u'\U0001F60D')
)

BOOLEAN_CHOICES = (
    (True, u'\U00002705'),
    (False, u'\U0000274C')
)

class Interaction(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.PROTECT, blank=False)
    turf = models.ForeignKey(Turf, on_delete=models.PROTECT, blank=False)
    at_home = models.BooleanField(choices=BOOLEAN_CHOICES, default=False)
    accepted_material = models.BooleanField(choices=BOOLEAN_CHOICES, default=False)
    campaign_response = models.SmallIntegerField(choices=RESPONSE_CHOICES, default=2)
    dsa_response = models.SmallIntegerField(choices=RESPONSE_CHOICES, default=2)
    campaign_info = JSONField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Parcel %s, Canvas %s' % (self.unit, self.canvas.name)

