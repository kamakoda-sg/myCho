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
	#url(r'^reserve/vendor/(?P<id>\d+)/?menu$','Cho.views.reserve_menu'),
	url(r'^reserve/vendor/(?P<id>\d+)/?spot$','Cho.views.reserve_spot'),
	url(r'^reserve/vendor/(?P<id>\d+)/?spot/confirm$','Cho.views.confirm_reserve'),
	url(r'^reserve/vendor/success$','Cho.views.reserve_success'),


	url(r'^my_account/(?P<id>\d+)?$','Cho.views.my_account'),
	url(r'^my_account/(?P<id>\d+)?/history','Cho.views.my_history'),
	url(r'^my_account/(?P<id>\d+)?/reviews','Cho.views.my_reviews'),
	url(r'^my_account/(?P<id>\d+)?/settings','Cho.views.my_settings'),
	url(r'^my_account/(?P<id>\d+)?/favourites','Cho.views.my_favourites'),

	url(r'^reviews/(\d+)?$','Cho.views.review_list'),
	url(r'^review_detail/(?P<id>\d+)/?$','Cho.views.review_detail'),


	url(r'^preorder/process_orders$','Cho.views.process_orders'),
	url(r'^delivery/process_delivery$','Cho.views.process_delivery'),
	url(r'^reserve/process_reservation$','Cho.views.process_reservation'),

	url(r'^preorder/vendor/confirmation$','Cho.views.confirmation'),













)
