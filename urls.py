from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^people/delay/(?P<person_id>\d+)/$', 'people.views.call_celery_delay', name='call-celery-delay'),
)
