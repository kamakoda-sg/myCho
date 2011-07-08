from django.db import models
from django.contrib import admin

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

class MenuCategory(models.Model):
	category = models.CharField(max_length=50)
	#JUST COMMENTED FOR TESTING SEE
	#post_items = models.ForeignKey(MenuItem)#list of items /array...

	def __unicode__(self):
		return self.category

class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	size = models.CharField(max_length=10)
	prize = models.IntegerField() # is there a float/double field?
	post_category = models.ForeignKey(MenuCategory)
	def __unicode__(self):
		return self.name+"\n size: "+self.size+"\n for "+str(self.prize)+" cedis"


class Menu(models.Model):
	#item = models.ForeignKey(MenuItem)
#	post_vendor = models.ForeignKey(Vendor)
	content = models.ForeignKey(MenuCategory)# this is rather supposed to be a listing of all menu categories and their items 	
	#can we use the item to get its category rather than making another foreign key to it?
	def __unicode__(self):
		return content+"wed check for vendor later"
	

class Vendor(models.Model):
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=80) # preferably models.EmailField
	rating = models.IntegerField()
	menu = models.ForeignKey(Menu)
	menu = []
#	menu_items = #list
	location = models.CharField(max_length=150)
#	details = #dict
#	history = #list
#	Categories = #list
	
	def __unicode__(self):
		return self.name+" menu "+menu
	def name_first_20(self):
		return self.name[:20]
'''
class MenuCategory(models.Model):
	category = models.CharField(max_length) #in actual terms should be  a list/array
'''


class Review(models.Model):
	#foreign key to users
	post_vendor = models.ForeignKey(Vendor)
#	ratings = models.IntegerField() # moved to the Vendor class as a one to one relationship
	review = models.TextField() # we shud probably add a max_length = 150..or sumfin
	
	def __unicode__(self):
		return self.review[:50]


class Delivery(models.Model):
	#foreign key to users
	post_vendor = models.ForeignKey(Vendor)
#	food_items = # list of items from the menu ; essentially a subset of the menu; chosing by the user
	#delete below...thats not the real one--> food_items!
	food_items = models.CharField(max_length=150)
	location = models.CharField(max_length=150)
	confirmation_code = models.IntegerField()
	
	def  __unicode__(self):
		return "Delivering "+food_items+" to "+ location

class Reservation(models.Model):
	#foreign key to users
	post_vendor = models.ForeignKey(Vendor)
	date = models.DateTimeField(auto_now=True)
	table = models.IntegerField()
	confirmation_code = models.IntegerField()
	
	def __unicode__(self):
		return "You have succesfully reserved "+table+" at "+post_vendor+"for "+date+".\n Your confirmation code is "+confirmation_code

class PreOrdering(models.Model):
	#foreign key to users
	post_vendor = models.ForeignKey(Vendor)
	ordered_items = models.CharField(max_length=200)#THIS SHOULD BE LIST ONLY LEFT HERE BECUASE OF UNICODE
	pick_up_time = models.DateTimeField(auto_now_add=True)#auto add now, incase you ever want to reset the time you would like to pick it up; can debate about whether it can/should be set...instead of using current time!
	confirmation_code = models.IntegerField()

	def __unicode__(self):
		return "You have succesfully preordered" +ordered_items+" from "+post_vendor+". Please do well to arrive at your pick up time "+pick_up_time+"\n Your 			confirmation code is "+confirmation_code #post_vendor.. may be a number...then we will figure how to ge the name of the vendor from that number

#actually search model...to have beenable to search between vendors, ratings etc
class VendorAdmin(admin.ModelAdmin):
	list_display = ('name_first_20','menu','rating')
	search_fields = ('name','rating')

class MenuItemAdmin(admin.ModelAdmin):
	list_display = ('name','post_category')

	


	
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Menu)
admin.site.register(MenuItem,MenuItemAdmin)
admin.site.register(MenuCategory)
admin.site.register(Delivery)
admin.site.register(Reservation)
admin.site.register(PreOrdering)

	
