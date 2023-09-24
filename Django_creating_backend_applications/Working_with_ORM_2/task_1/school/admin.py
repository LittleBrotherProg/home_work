from django.contrib import admin

from .models import Student, Teacher

class SchoolclassInLine(admin.TabularInline):
    model = Student.teachers.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        SchoolclassInLine
    ]
    exclude = ["teachers"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
