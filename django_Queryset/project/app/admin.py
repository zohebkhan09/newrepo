from django.contrib import admin
from .models import Student,Teacher


# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stu_name','stu_email','stu_city']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','stu_name','stu_email','stu_city']