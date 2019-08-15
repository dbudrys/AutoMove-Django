from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import CarDetails, CarImage, CarMake

from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

from django.contrib import messages

# Create your views here.
def index_page(request):
    carDetailsFull = CarDetails.objects.all().filter(prekyboje='Parduodama').order_by('-skelbimasSukurtas')[:12]
    #carDetailsFullSold = CarDetails.objects.all().exclude(prekyboje='Parduodama').exclude(prekyboje='Kita').order_by('-skelbimasSukurtas')[:6]
  
    context = {
        'carDetails' : carDetailsFull, 
        #'carDetailsSold': carDetailsFullSold,  
    }


    return render(request, 'cars/index.html', context)




def detailsOfCar(request, car_id):
    # car_id varable is manually created in urls.py 
    # and 'pk' attritube is going to match it with 'id' column in selected table
    # 'id' is automatically created by models.py
    carDetailsAll = get_object_or_404(CarDetails, pk=car_id)
    #carImageTest = CarImage.car_images.all()

    context = {
        'detail': carDetailsAll,
    }

    return render(request, 'cars/automobilioInfo.html', context) 

# New import for Paging
from django.core.paginator import Paginator

def automobiliaiVisi_page(request):
    #carDetailsFull = CarDetails.objects.all().filter(prekyboje='Parduodama').order_by('-skelbimasSukurtas')[:12]
    #carDetailsFullSold = CarDetails.objects.all().exclude(prekyboje='Parduodama').order_by('-skelbimasSukurtas')[:6]
    
    carTypeOnly = CarMake.objects.all().order_by('car_make')
    
    #Must be used for Pagination
    page = request.GET.get('page')

    if request.GET.get('select_type'):
        featured_filter = request.GET.get('select_type')
        carDetailsFull = CarDetails.objects.filter(automobilio_marke = featured_filter).filter(prekyboje='Parduodama').order_by('-skelbimasSukurtas')
        
        # Only for car count
        carCount = CarDetails.objects.filter(automobilio_marke = featured_filter).filter(prekyboje='Parduodama').count()

        # Used to set up page size
        paginator = Paginator(carDetailsFull, 200)

    else:
        carDetailsFull= CarDetails.objects.all().filter(prekyboje='Parduodama').order_by('-skelbimasSukurtas')
        
        # Only for car count
        carCount = CarDetails.objects.all().filter(prekyboje='Parduodama').count()

        # Used to set up page size
        paginator = Paginator(carDetailsFull, 24)



    carDetailsFullList = paginator.get_page(page)

    context = {
            'carDetails' : carDetailsFullList,
            'carTypeOnly' : carTypeOnly, 
            'carCount': carCount, 

            
        }

    return render(request, 'cars/automobiliai-visi.html', context)





def lizingoInformacija_page(request):
    return render(request, 'cars/lizingo-informacija.html')



# tutorial - https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/
# AND https://stackoverflow.com/questions/53332653/django-contact-form-with-bootstrap
def kontaktai_page(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_phone = form.cleaned_data['contact_phone']
            contact_message = form.cleaned_data['contact_message']

            # Email the profile with the
            # contact information
            template = get_template('cars/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'contact_message': contact_message,
            }
            content = template.render(context)

            email = EmailMessage(
                "Automotyvas.com Uzklausos Laiskas",
                content,
                "Automotyvas.com" +'',
                ['motyvasauto@gmail.com'],
                headers = {'Reply-To': contact_email }
            )

            # To display succesful message. Coming from messages modal

            messages.success(request, 'success_message')

            email.send()

            return redirect('kontaktai_page')

    return render(request, 'cars/susisiekti-kontaktai.html', {
        'form': form_class,
    })