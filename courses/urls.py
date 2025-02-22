from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.detail, name='course_details'),
    path('kategori/<int:category_id>', views.getCourseByCategoryId),
    path('kategori/<str:category_slug>', views.getCourseByCategory, name='courses_by_category'),
]