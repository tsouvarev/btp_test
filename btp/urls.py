from django.conf.urls import patterns, url

urlpatterns = patterns('hospital.views',
    url(r'^$', "get_all_data"),
    url(r'^get_spec_data/$', "get_spec_data", name="get_spec_data"),
)
