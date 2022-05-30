from django.urls import path
from .import views

urlpatterns = [
    path('meetups/',views.index)#add / as meetups/ for avoiding 404 error
]
