from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Anasayfa')

def iletisim(request):
    return HttpResponse('İletişim sayfası')

def hakkimizda(request):
    return HttpResponse('Hakkımızda sayfası')