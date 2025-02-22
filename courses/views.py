from datetime import datetime
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course, Category

def index(request):
    """Ana sayfa: Aktif kursları ve kategorileri listele"""
    kurslar = Course.objects.filter(isActive=True)
    kategoriler = Category.objects.all()
    
    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })

def detail(request, slug):
    """Belirli bir kursun detay sayfası"""
    course = get_object_or_404(Course, slug=slug)
    
    return render(request, 'courses/details.html', {'course': course})

def getCourseByCategory(request, category_slug):
    """Kategoriye göre kursları listele"""
    category = get_object_or_404(Category, slug=category_slug)
    courses = Course.objects.filter(isActive=True)  # Eğer kurslara kategori eklediysen: .filter(category=category)
    
    return render(request, 'courses/kurslar.html', {
        'category': category.name,
        'category_text': f"{category.name} kategorisindeki kurslar",
        'courses': courses
    })

def getCourseByCategoryId(request, category_id):
    """Kategori ID'ye göre yönlendirme yap"""
    category = get_object_or_404(Category, id=category_id)
    return redirect(reverse('courses_by_category', args=[category.slug]))