from django.contrib import admin

# Register your models here.
from first.models import Subject, Teacher


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('num', 'name', 'intro', 'is_hot')
    search_fields = ('name', )
    ordering = ('num', )


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('num', 'name', 'sex', 'birth', 'good_count', 'bad_count', 'subject')
    search_fields = ('name', )
    ordering = ('num', )


admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Teacher, TeacherModelAdmin)