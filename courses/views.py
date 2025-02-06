from django.http import HttpResponse
from django.shortcuts import render

def kurslar(request):
    return HttpResponse('Kurslar listesi')

def detail(request):
    return HttpResponse('Kurs detayı')

def programlama(request):
    return HttpResponse('Programlama kursu')

def mobiluygulamalar(request):  
    return HttpResponse('Mobil uygulamalar kursu')