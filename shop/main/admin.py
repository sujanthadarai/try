from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=['id','title']

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display=['id','image','name','price','decp','category']
