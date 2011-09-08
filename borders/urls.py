from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('borders.views',
    url(r'^mi/', 'view_map'),
    url(r'^data/', 'borders_data'),
)
