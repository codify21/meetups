from django.urls import path
from .import views

urlpatterns = [
    path('meetups/',views.index,name='all-meetups'), #add / at the end as meetups/ for avoiding 404 error
    path('meetups/success',views.confirm_registration,name='confirm-registration'),
    path('meetups/<slug:meetup_slug>',views.meetup_details,name='meetup-detail')
]
