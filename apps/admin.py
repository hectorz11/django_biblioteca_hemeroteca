from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
	list_display = ('id','code','authors','title','state')
	search_fields = ['code','authors','title']
	list_filter = ('classification','state')

class NewspaperAdmin(admin.ModelAdmin):
	list_display = ('id','volume','name','date_start','date_end','state')
	search_fields = ['volume','name']
	list_filter = ('classification','state','types')

admin.site.register(Classification)
admin.site.register(Location)
admin.site.register(State)
admin.site.register(Type)
admin.site.register(Book,BookAdmin)
admin.site.register(Newspaper,NewspaperAdmin)