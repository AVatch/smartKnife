from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r'^$', 'smartKnifeYoYo.view.homepage_view'),
)
