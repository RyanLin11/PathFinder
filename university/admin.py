from django.contrib import admin
from .models import University, Program, Application

# Register your models here.
admin.site.register(University)
admin.site.register(Program)
admin.site.register(Application)