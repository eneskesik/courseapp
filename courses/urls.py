from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('<kurs_adi>', views.detail),
    path('kategori/<int:category_id>', views.getCourseByCategoryId),
    path('kategori/<str:category_name>', views.getCourseByCategory),
]