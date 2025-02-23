from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SliderModel, AboutModel, ServicesModelCategory, ServicesModelEmployes, ProjectModels



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
