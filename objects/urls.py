from django.conf.urls import patterns, url

from objects.views import ObjectDetailView, ObjectCreateView, ObjectListView


urlpatterns = patterns('',
    url(r'^detail/$', ObjectDetailView.as_view(), name='object-detail'),
    url(r'^add/$', ObjectCreateView.as_view(), name='object-create'),
    url(r'^all/$', ObjectListView.as_view(), name='objects'),
    url(r'^add/(?P<pk>\d+)/$', 'objects.views.delete_object', name='delete_object')
)