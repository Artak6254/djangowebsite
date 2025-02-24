from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactUser
from .models import SliderModel, AboutModel, ServicesModelCategory, ServicesModelEmployes, ProjectModels, ContactForm



def indexView(requests):
    sliderData = SliderModel.objects.all()
    about = AboutModel.objects.all()
    services = ServicesModelCategory.objects.all()
    services_employee = ServicesModelEmployes.objects.all()
    project = ProjectModels.objects.all()
    
    
    context = {
        "sliderData": sliderData,
        "about": about,
        "services_category": services,
        "services_employee": services_employee,
        "project": project
    }
    for slider in sliderData:
        context['sliderData'] = slider
    return render(requests, 'index.html', context)


def detailView(requests):
    return render(requests, 'projectDetails.html')


from django.shortcuts import render, redirect
from .forms import ContactUser
from .models import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactUser(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_success', contact_id=contact.id)
        else:
            print("Form is not valid")
    else:
        form = ContactUser()
        
    return render(request, 'contact.html', {'form': form})

def contact_success(request, contact_id):
    contact = ContactForm.objects.get(id=contact_id)
    return render(request, 'contact.html', {'contact': contact})
