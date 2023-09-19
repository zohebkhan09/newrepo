from django.contrib import admin
from .models import AadharModel,StudentModel
# Register your models here.

@admin.site.register(AadharModel)
class AadharAdmin(admin.ModelAdmin):
    list_display=['id', 'aadhar_no']

admin.site.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['stu_name', 'aadhar_no']