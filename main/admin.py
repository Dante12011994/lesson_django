from django.contrib import admin

from main.models import Students, Subject


# admin.site.register(Students)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student',)
    list_filter = ('student',)
