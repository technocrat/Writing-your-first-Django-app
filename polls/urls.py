from django.conf.urls.defaults import *
from polls.models import Poll

info_dict = {
    'queryset': Poll.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)

from django.contrib import admin
admin.autodiscover()

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)

