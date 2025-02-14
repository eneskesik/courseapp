from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<kurs_adi>', views.detail),
    path('kategori/<int:category_id>', views.getCourseByCategoryId),
    path('kategori/<str:category_name>', views.getCourseByCategory, name='courses_by_category'),
]