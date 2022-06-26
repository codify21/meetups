
from django.contrib import admin
from .models import Snippet
# Register your models here.

# class MeetupAdmin(admin.ModelAdmin):
#     list_display=('title','slug','date','locationn')
#     list_filter = ('locationn','date')
#     prepopulated_fields={'slug':('title',)}

admin.site.register(Snippet)