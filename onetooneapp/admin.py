from django.contrib import admin
from.models import Student,Course
# Register your models here.
class Student_admin(admin.ModelAdmin):
    list_display = ['id','student_name','student_roll','student_email','student_mobile']
class Course_admin(admin.ModelAdmin):
    list_display = ['id','course_name','course_fee','course_duration']

admin.site.register(Student,Student_admin)
admin.site.register(Course,Course_admin)