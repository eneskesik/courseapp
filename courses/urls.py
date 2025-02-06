from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('detail', views.detail),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobiluygulamalar),
]