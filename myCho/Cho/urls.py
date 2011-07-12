from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'Cho.views.home'),
	url(r'^vendors/(\d+)?$','Cho.views.vendor_list'),
	url(r'^vendor_detail/(?P<id>\d+)/?$','Cho.views.vendor_detail'),
	url(r'^vendor/(?P<id>\d+)/?menu$','Cho.views.view_menu'),

#urls for PREORDER views
	url(r'^preorder/vendors?$','Cho.views.preorder'),
	url(r'^preorder/vendor/(?P<id>\d+)/?menu$','Cho.views.preorder_menu'),
	url(r'^preorder/vendor/(?P<id>\d+)/?menu/confirm$','Cho.views.confirm_order'),
#urls for DELIVERY views
	url(r'^delivery/vendors?$','Cho.views.delivery'),
	url(r'^delivery/vendor/(?P<id>\d+)/?menu$','Cho.views.delivery_menu'),
	url(r'^delivery/vendor/(?P<id>\d+)/?menu/confirm$','Cho.views.confirm_delivery'),
#urls for RESERVATION views
	url(r'^reserve/vendors?$','Cho.views.reserve'),
	url(r'^reserve/vendor/(?P<id>\d+)/?menu$','Cho.views.reserve_menu'),
	url(r'^reserve/vendor/(?P<id>\d+)/?menu/confirm$','Cho.views.confirm_reserve'),

	url(r'^my_account/(?P<id>\d+)?$','Cho.views.my_account'),

	url(r'^reviews/(\d+)?$','Cho.views.review_list'),
	url(r'^review_detail/(?P<id>\d+)/?$','Cho.views.review_detail'),



)
