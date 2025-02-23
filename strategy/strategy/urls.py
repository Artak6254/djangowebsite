from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('detail/', views.detailView, name="detail"),
    path('contact/', views.detailView, name="contact"),
    path('contact/success/<int:contact_id>/', views.detailView, name="contact"),
]