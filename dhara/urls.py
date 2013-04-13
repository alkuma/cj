from django.conf.urls import patterns, include, url

urlpatterns = patterns('dhara.views',
    url(r'^$', 'index'),
)
