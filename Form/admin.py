from django.contrib import admin

# Register your models here.
from .models import Student, College, Course, University


admin.site.register(Student)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(University)