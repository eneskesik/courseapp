from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render

data = {
    "programlama":"Programlama Kursları",
    "web-gelistirme":"Web Geliştirme Kursları",
    "mobil":"Mobil Uygulama Geliştirme Kursları",
}

def kurslar(request):
    return HttpResponse('Kurslar listesi')

def detail(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCourseByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Kategori bulunamadı")

def getCourseByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("Kategori bulunamadı")
    redirect_text = category_list[category_id - 1] 
    return redirect('/kurs/kategori/' + redirect_text)