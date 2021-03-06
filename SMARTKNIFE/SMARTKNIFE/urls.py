from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SMARTKNIFE.views.home', name='home'),
    # url(r'^SMARTKNIFE/', include('SMARTKNIFE.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
	url(r'^$', 'SMARTKNIFE.views.choose_page',name='choose'),
	url(r'^result/(?P<itemToSearch>\w+)/$', 'SMARTKNIFE.views.homepage_view',name='result'),
)
