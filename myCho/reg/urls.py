from django.conf.urls.defaults import *

urlpatterns = patterns('',
	#url(r'^$', 'Cho.views.home'),
	#url(r'^vendors/(\d+)?$','Cho.views.vendor_list'),
	url(r'^$','reg.views.home'),
	url(r'^sign_up$','reg.views.sign_up'),
	url(r'^login$','reg.views.log_in'),
	url(r'^logout/?$','reg.views.log_out'),
	url(r'^create/new_user$','reg.views.create_user'),

	#url(r'^sign_up$','reg.views.sign_up'),
	#url(r'^create/new_user$','reg.views.create_user'),
	#url(r'^login/$', 'reg.views.loginView'),








)
