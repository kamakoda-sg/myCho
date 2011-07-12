from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
     


class UserProfile(models.Model):
    location = models.TextField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
  # history = models.TextField()
  # favourites = models.TextField()
  # reviews = models.TextField()
  # ordered_items = models.TextField()
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
	return self.user.username



class History(models.Model):
	body  = models.TextField()
	user = models.ForeignKey(UserProfile)
	created = models.DateTimeField(auto_now_add=True)

	
	def __unicode__(self):
		return self.body





# Create your models here.

'''
Users:

location
username
password
email
history
review
favourites

'''

'''
class Menu(models.Model):
	#category = models.ForeignKey(MenuCategory)
	#menu_item = models.ForeignKey(MenuItem)
	#vendor = models.ForeignKey(Vendor)
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name+"'s Menu"
'''




class Vendor(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=80) # preferably models.EmailField
	rating = models.IntegerField()
	does_delivery = models.BooleanField()
	does_preordering = models.BooleanField()
	does_reservation = models.BooleanField()
#	menu = models.ForeignKey(Menu) Out!!!!!!!!!!!!!!!!!!!!
	location = models.CharField(max_length=150)
	#details = models.CharField(max_length=150)
	#history = models.TextField(max_length=700)
#	Categories = #list
	
	def __unicode__(self):
		return self.name
	def name_first_20(self):
		return self.name[:20]





class MenuCategory(models.Model):
	category = models.CharField(max_length=50)
	#menu = models.ForeignKey(Menu) OUT FOR GOOD
	vendor = models.ForeignKey(Vendor)
	#JUST COMMENTED FOR TESTING SEE
	#post_items = models.ForeignKey(MenuItem)#list of items /array...

	def __unicode__(self):
		return self.category

class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	size = models.CharField(max_length=10)
	price = models.DecimalField(decimal_places=2,max_digits=4)
	vendor = models.ForeignKey(Vendor)
	category = models.ForeignKey(MenuCategory)
	#menu = models.ForeignKey(Menu) OUT FOR GOOD!

	def __unicode__(self):
		return self.name+"\n size: "+self.size+"\n for "+str(self.price)+" cedis"



 


class Review(models.Model):
	body = models.TextField()
	author = models.ForeignKey(UserProfile)
	featured_vendor = models.ForeignKey(Vendor)
	created = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.body

	def body_first_60(self):
		return self.body[:60]


class Delivery(models.Model):
	vendor = models.ForeignKey(Vendor)
	food_items = models.CharField(max_length=150)
	location = models.CharField(max_length=150)
	recipient = models.ForeignKey(UserProfile)
	confirmation_code = models.IntegerField()
	
	def  __unicode__(self):
		return "Delivering "+food_items+" to "+ location

class Reservation(models.Model):
	vendor = models.ForeignKey(Vendor)
	date = models.DateTimeField(auto_now=False)
	table = models.IntegerField()
	person_reserving = models.ForeignKey(UserProfile)
	confirmation_code = models.IntegerField()
	
	def __unicode__(self):
		return "You have succesfully reserved "+table+" at "+vendor+"for "+date+".\n Your confirmation code is "+confirmation_code

class PreOrdering(models.Model):

	vendor = models.ForeignKey(Vendor)
	ordered_items = models.CharField(max_length=200)#THIS SHOULD BE LIST ONLY LEFT HERE BECUASE OF UNICODE
	pick_up_time = models.DateTimeField(auto_now_add=True)#auto add now, incase you ever want to reset the time you would like to pick it up; can debate about 
	recipient = models.ForeignKey(UserProfile)
	confirmation_code = models.IntegerField()


	def __unicode__(self):
		return "You have succesfully preordered" +ordered_items+" from "+vendor+". Please do well to arrive at your pick up time "+pick_up_time+"\n Your 			confirmation code is "+confirmation_code #post_vendor.. may be a number...then we will figure how to ge the name of the vendor from that number




#actually search model...to have beenable to search between vendors, ratings etc
class VendorAdmin(admin.ModelAdmin):
	list_display = ('name_first_20','rating')
	search_fields = ('name','rating')

class MenuItemAdmin(admin.ModelAdmin):
	list_display = ('name','category',)

	
class MenuCategoryAdmin(admin.ModelAdmin):
	list_display = ('category','vendor')

admin.site.register(UserProfile)
admin.site.register(History)	
admin.site.register(Review)
admin.site.register(Vendor,VendorAdmin)
#admin.site.register(Menu)
admin.site.register(MenuItem,MenuItemAdmin)
admin.site.register(MenuCategory,MenuCategoryAdmin)
admin.site.register(Delivery)
admin.site.register(Reservation)
admin.site.register(PreOrdering)

	
