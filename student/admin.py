from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StuClass,StudentUser



admin.site.register(StudentUser)
admin.site.register(StuClass)
# Register your models here.
