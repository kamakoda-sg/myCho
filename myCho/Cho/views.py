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




def vendor_list(request,limit=100):
	vendor_list = Vendor.objects.all()
	t = loader.get_template('Cho/vendors.html')
	c = Context({'vendor_list':vendor_list})
	return HttpResponse(t.render(c))




'''@csrf_exempt
def blog_detail(request,id,showComments=False):
	blog = Blog.objects.get(pk = id)
	t = loader.get_template('blog/detail.html')
	if request.method == 'POST':
		comment = Comment(post=blog)
		comment.author = request.user

		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:	
		if request.user.is_authenticated:	
			form = CommentForm()
			c = Context({'blog':blog,'comments':comments,'form':form.as_p(),'logged_in':request.user.is_authenticated,'author':request.user,'request':request})
		
	c = Context({'blog':blog,'comments':comments,'user':str(request.user),'logged_in':request.user.is_authenticated,'request':request})
	return HttpResponse(t.render(c))
'''






def vendor_detail(request,id):
	vendor = Vendor.objects.get(pk=id)
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
