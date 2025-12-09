from django.contrib import admin
from .models import Student
from .models import teachers


admin.site.register(Student)
admin.site.register(teachers)

# Register your models here.
