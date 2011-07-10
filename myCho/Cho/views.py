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
from models import UserProfile,History, Menu,  MenuCategory,MenuItem, Vendor,Review,  Delivery, Reservation, PreOrdering


def home(request):
	t = loader.get_template('Cho/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))



# Create your views here.
