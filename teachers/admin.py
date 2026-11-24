from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "subject")
    search_fields = ("first_name", "last_name", "email", "subject")
