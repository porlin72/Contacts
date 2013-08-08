from django.contrib import admin
from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ('user','first_name','last_name','number')
	
admin.site.register(Contact, ContactAdmin)