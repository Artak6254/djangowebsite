from django.db import models

# Create your models here.

class SliderModel(models.Model):
    banner_slider = models.URLField()
    project = models.CharField(max_length=50)
    text  = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.project} {self.text}"
    
class AboutModel(models.Model): 
    agency_image = models.URLField()
    agency_specialist = models.CharField(max_length=50)
    agency_fullname = models.CharField(max_length=60)
    agency_text = models.CharField(max_length=150)
    agency_about_title = models.CharField(max_length=100)
    agency_about_heading = models.CharField(max_length=200)
    agency_buisbusines = models.CharField(max_length=200)
    agency_dec = models.TextField()
    business_dolor = models.CharField(max_length=100)
    about_us = models.CharField(max_length=100)
    about_text = models.TextField()
    
    def __str__(self):
        return (  
            f"{self.agency_specialist} {self.agency_fullname} "
            f"{self.agency_text} {self.agency_about_title} {self.agency_about_heading} "
            f"{self.agency_buisbusines} {self.agency_dec} {self.business_dolor} "
            f"{self.about_us} {self.about_text}"
        )

    
class ServicesModelCategory(models.Model):
    buisnes_consulting = models.CharField(max_length=255)
    buisnes_text = models.TextField()
    
    def __str__(self):
        return f"{self.buisnes_consulting} {self.buisnes_text}"

class ServicesModelEmployes(models.Model):
    services_image = models.URLField()
    services_title = models.CharField(max_length=120)
    consulting_points = models.TextField()
    
    def __str__(self):
        return f"{self.services_image} {self.services_title} {self.consulting_points}"         
                
                
class ProjectModels(models.Model):
    project_image = models.URLField()
    project_title = models.CharField(max_length=100)
    project_heading = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.project_image} {self.project_title} {self.project_heading}"  
    
                        