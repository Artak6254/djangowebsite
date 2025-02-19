from django.contrib import admin
from .models import SliderModel, AboutModel, ServicesModelCategory, ServicesModelEmployes, ProjectModels


# Register your models here.
admin.site.register(SliderModel)
admin.site.register(AboutModel)
admin.site.register(ServicesModelCategory)
admin.site.register(ServicesModelEmployes)
admin.site.register(ProjectModels)