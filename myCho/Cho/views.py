'''
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
#from django.contrib.auth.decorators import login_required
from models import Blog, Comment
'''


from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import UserProfile,History,  MenuCategory,MenuItem, Vendor,Review,  Delivery, Reservation, PreOrdering


def home(request):
	t = loader.get_template('Cho/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))




def vendor_list(request,limit=100):
	vendor_list = Vendor.objects.all()
	t = loader.get_template('Cho/vendors.html')
	c = Context({'vendor_list':vendor_list})
	return HttpResponse(t.render(c))



def vendor_detail(request,id):
	vendor = Vendor.objects.get(pk=id)
#	menu = Menu.objects.filter(vendor__pk=id)
#	menu=""
	t = loader.get_template('Cho/vendor_detail.html')
	c = Context({'vendor':vendor})
	return HttpResponse(t.render(c))

def view_menu(request,id):
	vendor = Vendor.objects.get(pk=id)
	#key = vendor.id
	#pulling all categories that belong to the vendor
	#
	menu_categories = MenuCategory.objects.filter(vendor__pk=id)
	menu_items = MenuItem.objects.filter(category__pk=id)
#	menu_items = MenuItem.objects.filter(vendor__pk=id)

	t = loader.get_template('Cho/view_menu.html')	
	c = Context({'vendor':vendor,'categories':menu_categories,'items':menu_items})
	return HttpResponse(t.render(c))


def preorder(request):
	vendors = Vendor.objects.all()
	
	t = loader.get_template('Cho/preorder/vendors.html')
	c = Context({'vendors': vendors})
	return HttpResponse(t.render(c))

def preorder_menu(request,id):
	categories = MenuCategory.objects.filter(vendor__pk=id)
	items = MenuItem.objects.filter(vendor__pk=id)
	vendor = Vendor.objects.get(pk=id)
	t = loader.get_template('Cho/preorder/vendor/menu.html')
	c = Context({'categories':categories,'items':items,'vendor':vendor})
	return HttpResponse(t.render(c))

def confirm_order(request,id):
	t = loader.get_template('Cho/preorder/vendor/dialog.html')
	c = Context(dict())
	return HttpResponse(t.render(c))




def delivery(request):
	vendors = Vendor.objects.all()
	
	t = loader.get_template('Cho/delivery/vendors.html')
	c = Context({'vendors': vendors})
	return HttpResponse(t.render(c))

def delivery_menu(request,id):
	categories = MenuCategory.objects.filter(vendor__pk=id)
	items = MenuItem.objects.filter(vendor__pk=id)
	vendor = Vendor.objects.get(pk=id)
	t = loader.get_template('Cho/delivery/vendor/menu.html')
	c = Context({'categories':categories,'items':items,'vendor':vendor})
	return HttpResponse(t.render(c))

def confirm_delivery(request,id):
	t = loader.get_template('Cho/delivery/vendor/dialog.html')
	c = Context(dict())
	return HttpResponse(t.render(c))






def reserve(request):
	vendors = Vendor.objects.all()
	
	t = loader.get_template('Cho/reserve/vendors.html')
	c = Context({'vendors': vendors})
	return HttpResponse(t.render(c))

def reserve_menu(request,id):
	categories = MenuCategory.objects.filter(vendor__pk=id)
	items = MenuItem.objects.filter(vendor__pk=id)
	vendor = Vendor.objects.get(pk=id)
	t = loader.get_template('Cho/reserve/vendor/menu.html')
	c = Context({'categories':categories,'items':items,'vendor':vendor})
	return HttpResponse(t.render(c))

def confirm_reserve(request,id):
	t = loader.get_template('Cho/reserve/vendor/dialog.html')
	c = Context(dict())
	return HttpResponse(t.render(c))


def my_account(request,id):
	user_profile = UserProfile.objects.get(pk=id)
	t = loader.get_template('Cho/my_account.html')
	c = Context({'user':user_profile})
	return HttpResponse(t.render(c))

def review_list(request,limit=100):
	review_list = Review.objects.all()
	vendors = Vendor.objects.all()
	t = loader.get_template('Cho/reviews.html')
	c = Context({'review_list':review_list,'vendors':vendors})
	return HttpResponse(t.render(c))

def review_detail(request,id):
	review = Review.objects.get(pk=id)
	#vendor = Vendor.objects.get(pk=id)
	t = loader.get_template('Cho/review_detail.html')
	c = Context({'review':review})
	return HttpResponse(t.render(c))
	
# Create your views here.
