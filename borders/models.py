from django.contrib.gis.db import models


# This is an auto-generated Django model module created by ogrinspect.
class BordersMI(models.Model):
    statefp10 = models.CharField(max_length=2)
    countyfp10 = models.CharField(max_length=3)
    cousubfp10 = models.CharField(max_length=5)
    cousubns10 = models.CharField(max_length=8)
    geoid10 = models.CharField(max_length=10)
    name10 = models.CharField(max_length=100)
    namelsad10 = models.CharField(max_length=100)
    lsad10 = models.CharField(max_length=2)
    classfp10 = models.CharField(max_length=2)
    mtfcc10 = models.CharField(max_length=5)
    cnectafp10 = models.CharField(max_length=3)
    nectafp10 = models.CharField(max_length=5)
    nctadvfp10 = models.CharField(max_length=5)
    funcstat10 = models.CharField(max_length=1)
    aland10 = models.FloatField()
    awater10 = models.FloatField()
    intptlat10 = models.CharField(max_length=11)
    intptlon10 = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

    def __unicode__(self):
	return self.name10


