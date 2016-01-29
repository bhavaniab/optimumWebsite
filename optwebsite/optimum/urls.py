from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(template_name='optimum/index.html'),name='index'),
)
