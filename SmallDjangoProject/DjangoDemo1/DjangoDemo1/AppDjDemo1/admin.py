from django.contrib import admin

# Register your models here.
from .models import Plan_Tasks, Item

admin.site.register(Plan_Tasks)
admin.site.register(Item)