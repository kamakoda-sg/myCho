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
from models import UserProfile,History,  MenuCategory,MenuItem, Vendor,Review,  Delivery, Reservation, PreOrdering, Spot
import random







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
	menu_items = MenuItem.objects.filter(vendor__pk=id)

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

def reserve_spot(request,id):
	#categories = MenuCategory.objects.filter(vendor__pk=id)
	#items = MenuItem.objects.filter(vendor__pk=id)
	spots = Spot.objects.filter(vendor__pk=id)	
	vendor = Vendor.objects.get(pk=id)
	t = loader.get_template('Cho/reserve/vendor/spot.html')
	c = Context({'spots':spots,'vendor':vendor})
	return HttpResponse(t.render(c))

def confirm_reserve(request,id):
	t = loader.get_template('Cho/reserve/vendor/dialog.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

def reserve_success(request):
	t = loader.get_template('Cho/reserve/vendor/success.html')
	c = Context(dict())
	return HttpResponse(t.render(c))



def my_account(request,id):
	user_profile = UserProfile.objects.get(pk=id)
	t = loader.get_template('Cho/my_account.html')
	c = Context({'user':user_profile})
	return HttpResponse(t.render(c))

def my_history(request,id):
	if request.user.is_authenticated:
		preorders = PreOrdering.objects.filter(recipient__pk=id)
		deliveries = Delivery.objects.filter(recipient__pk=id)
		reservations = Reservation.objects.filter(person_reserving__pk=id)
		t = loader.get_template('Cho/my_account/history.html')
		c = Context({'orders':preorders,'deliveries':deliveries,'reservations':reservations})
		return HttpResponse(t.render(c))
	else:
		return HttpResponse("You are NOT Logged in! Please do")

def my_settings(request,id):
	t = loader.get_template("Cho/my_account/settings.html")
	c = Context(dict())
	return HttpResponse(t.render(c))

def my_reviews(request,id):
	reviews = Review.objects.filter(author__pk=id)
	t = loader.get_template('Cho/my_account/reviews.html')
	c = Context({'reviews':reviews})
	return HttpResponse(t.render(c))

def my_favourites(request,id):
	text = "Your favourites would have appeared here if you had any... lol!"
	t = loader.get_template('Cho/my_account/favourites.html')
	c = Context({'text':text})
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


class PreOrderForm(ModelForm):
	class Meta:
		model = PreOrdering

@csrf_exempt
def process_orders(request):
	print "process_orders"
	if request.method == 'POST':
		items = request.POST
		#t = loader.get_template('Cho/orders.html')NO LONGER REDIRECTING HERE.. BUT WILL NEED TO COME BACK INORDER TO WORK ON PURCHASE CONFIRMATION ETC..
		t = loader.get_template('Cho/base.html')
		c = Context({'items':items})
		print request.POST
		vendor = Vendor.objects.get(pk=request.POST['sec_key'])
		order_list= []

		for k,v in request.POST.iteritems():
			if k == "sec_key":
				print "it is"
				pass
			else:
				order_list.append(int(k[len('checkbox_'):]))
		print order_list

		order = ""
		for orders in order_list:
			order += str(MenuItem.objects.get(pk=orders))+" \n"
			print MenuItem.objects.get(pk=orders)
#		for order in order_list:
#CONTINUE TODAY... HAVE A LOOP THROUH ORDER LIST AND PICK THE ORDERS AS A \N SEPERATED STRING AND PASS AS CONTEXT..IN FUTURE TRY TO FIX THIS IN THE ELSE STATEMENT ABOVE..
				
		#/**Hardcoded user 1 **/
		userProfile = UserProfile.objects.get(pk=1)
#newstudent = Student.objects.create(name='Afram Sucks',age=4)
		code = str(vendor.id)+ str(random.randint(7500, 8000))
		order = PreOrdering.objects.create(vendor=vendor,ordered_items=order, pick_up_time='2006-10-25 14:30:59',recipient=userProfile,confirmation_code=code)
		print "CAME THRU"
		return HttpResponse(t.render(c))

	return HttpResponse()
	
@csrf_exempt
def process_delivery(request):
	print "process delivery"
	if request.method == 'POST':
		print request.POST
		print "posted delivery"
	t = loader.get_template('Cho/base.html')
	c = Context(dict())
	vendor = Vendor.objects.get(pk=request.POST['sec_key'])
	location = request.POST['deliveryLocation']
	delivery_list = []

	for k,v in request.POST.iteritems():
		if k == "sec_key":
			print "it has a secret key"
			pass
		elif k == "deliveryLocation":
			print "has a delivery location"
		else:
			delivery_list.append(int(k[len('checkbox_'):]))
	print delivery_list,"....."
	delivery = ""
	for deliveries in delivery_list:
		delivery += str(MenuItem.objects.get(pk = deliveries))+"\n"
	print "your deliveries are..", delivery
	#/**Hardcoded user 1 **/
	userProfile = UserProfile.objects.get(pk=1)
	code = str(vendor.id)+ str(random.randint(8001, 8500))
	final_delivery = Delivery.objects.create(vendor=vendor,food_items=delivery,location=location,recipient=userProfile,confirmation_code=code)
	print "delivery came thru!!!"

	return HttpResponse(t.render(c)) 


@csrf_exempt
def process_reservation(request):
	print "process reservation"
	if request.method == 'POST':
		print request.POST
		print "posted reservation"
	t = loader.get_template('Cho/base.html')
	c = Context(dict())
	vendor = Vendor.objects.get(pk=request.POST['sec_key'])
	reservation_list = []
	reservation = ""
	
	for k,v in request.POST.iteritems():
		if k == "sec_key":
			print "it also has a secret key"
			pass
		else:
			reservation_list.append(int(k[len('checkbox_'):]))
			print k[len('checkbox_'):],"is...."
			reservation +=str(Spot.objects.get(pk=k[len('checkbox_'):]))+" \n"
	print reservation_list,"***"
	print "and rreservation is..",reservation
	#/**Hardcoded user 1 **/
	userProfile = UserProfile.objects.get(pk=1)
	code = str(vendor.id)+ str(random.randint(9001, 9500))
	final_reservation = Reservation.objects.create(vendor=vendor,person_reserving=userProfile,confirmation_code=code, selected_spots=reservation)

	return HttpResponse(t.render(c))

def confirmation(request):
	t = loader.get_template("/cho/preorder/vendor/confirmation.html")
	c = Context(dict())
#	render_to_response("Cho/preorder/vendor/confirmation.html")
	return HttpResponse(t.render(c))
# Create your views here.
