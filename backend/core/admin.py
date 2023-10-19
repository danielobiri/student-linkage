from django.contrib import admin

# Register your models here.
from core.models import University, Course, Degree, Profile, Job

admin.site.register(University)
admin.site.register(Course)
admin.site.register(Degree)
admin.site.register(Profile)
admin.site.register(Job)
