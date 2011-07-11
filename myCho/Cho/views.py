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
	menu_categories = MenuCategory.objects.filter(menu__pk=id)
	menu_items = MenuItem.objects.filter(category__pk=id)

	t = loader.get_template('Cho/view_menu.html')	
	c = Context({'vendor':vendor,'categories':menu_categories,'items':menu_items})
	return HttpResponse(t.render(c))

# Create your views here.
