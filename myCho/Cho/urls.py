from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'Cho.views.home'),
	url(r'^vendors/(\d+)?$','Cho.views.vendor_list'),
	url(r'^vendor_detail/(?P<id>\d+)/?$','Cho.views.vendor_detail'),
	url(r'^vendor/(?P<id>\d+)/?menu$','Cho.views.view_menu'),


)
