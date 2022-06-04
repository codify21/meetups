from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
from .forms import RegistrationForm

# Create your views here.

def index(request):
    
    meetups = Meetup.objects.all()
    
    # meetups =[
    #     {'title':'A First meetup',
    #     'location':'New York',
    #     'slug':'a-first-meetup'
    #     },
    #     {'title':'A second meetup',
    #     'location':'Paris',
    #     'slug':'a-second-meetup'
    #     },
    #     {'title':'A third meetup',
    #     'location':'Mexico',
    #     'slug':'a-third-meetup'
    #     }
    # ]
    return render(request,'meetups/index.html',{
        'show_meetups': True,
        'meetups':meetups})

def meetup_details(request,meetup_slug):
     # selected_item ={ 
    #     'title':'A First Meetup',
    #     'description':'This is the first meetup'
    #     }
    try:
        selected_item =  Meetup.objects.get(slug= meetup_slug)
        registration_form = RegistrationForm()
        return render(request,'meetups/meetup-details.html',{
            # 'meetup_title':selected_item['title'],
            # 'meetup_title':selected_item.title,
            # 'meetup_description':selected_item['description']
            # 'meetup_description':selected_item.description,
            'meetup_found':True,
            'meetup':selected_item,#interacting directly with model except passing values,
            'form': registration_form,
        })
    except Exception as exc:
         return render(request,'meetups/meetup-details.html',{
          'meetup_found':False,
         })

