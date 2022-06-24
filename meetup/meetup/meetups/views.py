from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup,Participant,Users
from .forms import RegistrationForm,LoginForm

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
        if request.method=='GET':          
            registration_form = RegistrationForm()
            
        else:
            registration_form = RegistrationForm(request.POST)
            print('---')
            if registration_form.is_valid():
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant,_ = Participant.objects.get_or_create(email=user_email)
                print(participant,'---')
                selected_item.participantss.add(participant)
                return redirect('confirm-registration',meetup_slugg= meetup_slug)
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

def confirm_registration(request,meetup_slugg):
    meetup = Meetup.objects.get(slug= meetup_slugg)
    return render(request,'meetups/registration-success.html',{
        'organizer_email':meetup.organizer_email,
    })

def login(request):
    
    # if request.method == 'POST': Normal case
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     print(email,'----',password)

    if request.method == 'POST': #For storing data using forms.Form
        try:
            form = LoginForm(request.POST) 
            # form = LoginForm(request.POST,instance = existing_login  )
            if form.is_valid():           
                # user=Users(       #saving data to model
                #     email=form.cleaned_data['email'],
                #     password=form.cleaned_data['password'])
                # user.save()
                
                online_user_email = form.cleaned_data['email'] 
                online_user_password = form.cleaned_data['password']
                # print(online_user_email,online_user_password)
                if Users.objects.filter(email=online_user_email).exists():
                        model_email = Users.objects.filter(email=online_user_email).values()
                        model_password = model_email[0]['password']
        
                        if online_user_password==model_password:
                            return index(request)
                        else:
                            return render(request,'meetups/login.html',{
                                    'error':'Enter correct password',
                                    'is_true':True,
                                })
                        
                else:
                    return render(request,'meetups/register.html',{'form':form})

                # except Exception as e:
                #     # print(e)
                #     return render(request,'meetups/register.html',{'form':form})

                return render(request,'meetups/login.html',{'form':form})
        except Exceptions as exc:
            print(exc)
            return render(request,'meetups/login.html',{'form':form})



    # if request.method == 'POST':#For storing data using forms.ModelForm
    #     form = LoginForm(request.POST)# also u could modify easily using instance keyword  inside LoginForm
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()

   

    form = LoginForm()

    return render(request,'meetups/login.html',{'form':form})

def register(request):
    return render(request,'meetups/register.html',{'form':form})
