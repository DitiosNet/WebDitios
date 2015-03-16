from django.conf.urls import patterns, include, url
from .views import index, servicios, contacto

urlpatterns = patterns('',
    url(r'^$', index.as_view()),
    url(r'^servicios/', servicios.as_view()),
    url(r'^contacto/', contacto.as_view()),
)
