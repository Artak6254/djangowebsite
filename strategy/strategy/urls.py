from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('detail/', views.detailView, name="detail"),
    path('contact/', views.contact, name="contact"),
    path('contact/success/<int:contact_id>/', views.contact_success, name="contact_success"),
]