# Create your views here.



from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
#from models import UserProfile,History,  MenuCategory,MenuItem, Vendor,Review,  Delivery, Reservation, PreOrdering, Spot
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from Cho.models import UserProfile


import django.contrib.auth




class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	phone_number = forms.CharField(max_length=10)
	email = forms.EmailField()



@csrf_exempt
def home(request):
	if request.method == 'POST':
		uname = request.POST['username']
		pword = request.POST['password']
		user = authenticate(username = uname,password = pword)
		
		if user is not None:
			login(request,user)
			#then redirect
			print request.user.is_authenticated()," ....."
			print request.user
			#PROBABLY WHERE I SHOULD INITIALIZE USER PROFILE OBJECT TO USER??
			#added user to the context....
			return render_to_response('Reg/home.html',{'logged_in': request.user.is_authenticated(),'user':uname})
		else:
			return HttpResponse("Invalid user credentials")
			

	form = LoginForm()
	return render_to_response('Reg/home.html',{'form':form.as_p()})



@csrf_exempt
def log_in(request):
	if request.method == 'POST':
		uname = request.POST['username']
		pword = request.POST['password']
		user = authenticate(username = uname,password= pword)
		
		if user is not None:
			login(request,user)
			return render_to_response('Cho/base.html',{'logged_in': request.user.is_authenticated(),'user':uname})
		else:
			return HttpResponse("Sorry, Invalid user credentials")
	form = LoginForm()
	return render_to_response('Reg/home.html',{'form':form.as_p()})


@csrf_exempt
def log_out(request):
	logout(request)
	t = loader.get_template('Reg/logout.html')
	c = Context(dict())
	return HttpResponse(t.render(c))
	

@csrf_exempt
def sign_up(request):
#	t = loader.get_template("reg/create_user.html")
#	c = Context(dict())
	form = SignUpForm()
#	user = User.objects.create(username="adfga",password="pps",email="kwame.owusuafram@gmail.com")
#	userProfile = UserProfile.objects.create(location="osu",phone_number="0",email=user.email,user=user)
	return render_to_response('Reg/create_user.html',{'form':form.as_p()})


@csrf_exempt
def create_user(request):
	if request.method == 'POST':
		print request.POST
		print "postinn" 
	
	user = User.objects.create(username="wwkmsgdfga",password="pps",email="kwame.owusuafram@gmail.com")
	#login(request,user)
	userProfile = UserProfile.objects.create(location="india",phone_number="01",email=user.email,user=user)
#	t = loader.get_template("Cho/base.html")
#	c = Context({'userProfile':userProfile})
#	return HttpResponse(t.render(c))
	return render_to_response('Cho/base.html',{'userProfile':userProfile})
'''
def home(request):
	t = loader.get_template("Reg/home.html")
	c = Context(dict())
	return HttpResponse(t.render(c))
'''	

