from django.contrib.gis.db import models

# Create your models here.
class Facility(models.Model):
    location_id = models.IntegerField(null=True, blank=True)
    applicant = models.CharField(null=True, blank=True, max_length=500)
    facility_type = models.CharField(null=True, blank=True, max_length=200)
    cnn = models.IntegerField(null=True, blank=True)
    location_description = models.CharField(null=True, blank=True, max_length=500)
    address = models.CharField(null=True, blank=True, max_length=500)
    blocklot = models.CharField(null=True, blank=True, max_length=200)
    block = models.CharField(null=True, blank=True, max_length=200)
    lot = models.CharField(null=True, blank=True, max_length=200)
    permit = models.CharField(null=True, blank=True, max_length=200)
    status = models.CharField(null=True, blank=True, max_length=200)
    foodItems = models.CharField(null=True, blank=True, max_length=1000)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    point = models.PointField(null=True, blank=True, srid=4326)
    schedule = models.CharField(null=True, blank=True, max_length=1000)
    dayshours = models.CharField(null=True, blank=True, max_length=200)
    noi_sent = models.CharField(null=True, blank=True, max_length=200)
    approved = models.CharField(null=True, blank=True, max_length=200)
    received = models.IntegerField(null=True, blank=True)
    prior_permit = models.IntegerField(null=True, blank=True)
    expiration_date = models.CharField(null=True, blank=True, max_length=200)
    location = models.CharField(null=True, blank=True, max_length=200)
    fire_prevention_districts = models.IntegerField(null=True, blank=True)
    police_districts = models.IntegerField(null=True, blank=True)
    supervisor_districts = models.IntegerField(null=True, blank=True)
    zip_codes = models.IntegerField(null=True, blank=True)
    neighborhoods_old = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

