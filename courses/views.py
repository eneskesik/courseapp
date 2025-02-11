from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama":"Programlama Kursları",
    "web-gelistirme":"Web Geliştirme Kursları",
    "mobil":"Mobil Uygulama Geliştirme Kursları",
}

def index(request):
    return render(request, 'courses/index.html')

def kurslar(request):
    list_items = ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f'<li><a href="{redirect_url}">{category}</a></li>'

    html = f'''
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kurs Listesi</title>
    </head>
    <body>
        <h1>Kurs Listesi</h1>
        <ul>{list_items}</ul>
    </body>
    </html>
    '''

    return HttpResponse(html)

def detail(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCourseByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("<h1>Kategori bulunamadı<h1>")

def getCourseByCategoryId(request, category_id):
    category_list = list(data.keys())
    if (category_id > len(category_list)):
        return HttpResponseNotFound("<h1>Kategori bulunamadı<h1>")
    category_name = category_list[category_id - 1] 

    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)