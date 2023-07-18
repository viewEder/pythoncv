from django.contrib import admin
from .models import Stack, Academy, EmploymentHistory, ProjectDev, HobbiesExtras, Skills

# Register your models here.
admin.site.register(Stack)
admin.site.register(Academy)
admin.site.register(EmploymentHistory)
admin.site.register(ProjectDev)
admin.site.register(HobbiesExtras)
admin.site.register(Skills)