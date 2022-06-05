from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name='login'),
    # path('',views.index,name='all-meetups'), #add / at the end as meetups/ for avoiding 404 error
    path('<slug:meetup_slugg>/success',views.confirm_registration,name='confirm-registration'),
    path('<slug:meetup_slug>',views.meetup_details,name='meetup-detail')
]
