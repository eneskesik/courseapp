from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama":"Programlama Kursları",
    "web-gelistirme":"Web Geliştirme Kursları",
    "mobil":"Mobil Uygulama Geliştirme Kursları",
}
def index(request):
    list_items = ""
    category_list = list(data.keys())

    return render(request, 'courses/index.html', {
        'categories': category_list
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