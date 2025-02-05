from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Anasayfa')

def kurslar(request):
    return HttpResponse('Kurslar listesi')