from django.contrib import admin
from .models import Meetup,Location,Participant,Users
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display=('title','slug','date','locationn')
    list_filter = ('locationn','date')
    prepopulated_fields={'slug':('title',)}

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Users)
