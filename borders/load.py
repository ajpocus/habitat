import os
from django.contrib.gis.utils import LayerMapping
from borders.models import BordersMI

# Auto-generated `LayerMapping` dictionary for MIBorders model
mi_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'cousubfp10' : 'COUSUBFP10',
    'cousubns10' : 'COUSUBNS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'cnectafp10' : 'CNECTAFP10',
    'nectafp10' : 'NECTAFP10',
    'nctadvfp10' : 'NCTADVFP10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON',
}

mi_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    'data/mi/tl_2010_26_cousub10.shp'))

def run(verbose=True):
    lm = LayerMapping(BordersMI, mi_shp, mi_mapping, transform=False,
	encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

