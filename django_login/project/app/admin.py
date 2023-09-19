from django.contrib import admin
from app.models import User
from .models import Student,Teacher
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('Firstname','Lastname','Email','Contact','Password')

admin.site.register(User,UserAdmin)



# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stu_name','stu_email','stu_city']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','stu_name','stu_email','stu_city']