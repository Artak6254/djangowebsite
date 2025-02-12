from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SliderModel, AboutModel, ServicesModelCategory, ServicesModelEmployes, ProjectModels



def indexView(requests):
    sliderData = SliderModel.objects.all()
    context = {
        "sliderData": sliderData
    }
    return render(requests, 'strategy/index.html', context)
