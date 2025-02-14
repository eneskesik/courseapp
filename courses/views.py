from datetime import date, datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama":"Programlama Kursları",
    "web gelistirme":"Web Geliştirme Kursları",
    "mobil uygulamalar":"Mobil Uygulama Geliştirme Kursları",
}

db = {
    "courses": [
        {
            "title":"javascript kursu",
            "description":"javascript kursu açıklaması",
            "image":"1.jpg",
            "slug":"javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title":"python kursu",
            "description":"python kursu açıklaması",
            "image":"2.jpg",
            "slug":"python-kursu",
            "date": date(2022,9,10),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kursu açıklaması",
            "image":"3.jpg",
            "slug":"web-gelistirme-kursu",
            "date": date(2022,8,10),
            "isActive": True,
            "isUpdated": True
        }

    ],
    "categories": [
        {"id": 1, "name": "programlama", "slug": "programlama"},
        {"id": 2, "name": "web gelistirme", "slug": "web gelistirme"},
        {"id": 3, "name": "mobil uygulamalar", "slug": "mobil uygulamalar"},
         ]
}

def index(request):
    # list comphension
    kurslar = [course for course in db["courses"] if course["isActive"]==True]
    kategoriler = db["categories"]

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })

def detail(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCourseByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/kurslar.html', {
            'category': category_name,
            'category_text': category_text})
    except:
        return HttpResponseNotFound("<h1>Kategori bulunamadı<h1>")

def getCourseByCategoryId(request, category_id):
    category_list = list(data.keys())
    if (category_id > len(category_list)):
        return HttpResponseNotFound("<h1>Kategori bulunamadı<h1>")
    category_name = category_list[category_id - 1] 

    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)