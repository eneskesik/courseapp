from django.db import models
from datetime import datetime, date
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default='',blank= True, editable= False, null=False, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, blank=True, null=False, editable= False, db_index=True, default='')
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.name)  # Eğer slug boşsa otomatik oluştur
        elif self.pk:  # Eğer zaten bir obje mevcutsa (güncelleme yapılıyorsa)
            self.slug = slugify(self.name)  # Slug'ı name'e göre güncelle
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name}"