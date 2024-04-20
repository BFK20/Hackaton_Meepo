from django.contrib import admin

from .models import Department, Group, Faculty, vuses

class GroupInline(admin.TabularInline):
    extra = 1
    model = Group

class DepartmentInline(admin.TabularInline):
    extra = 1
    model = Department
    inlines = [GroupInline]
    fields = 'name',


class FacultyInline(admin.StackedInline):
    extra = 1
    model = Faculty
    inlines = [DepartmentInline]
    fields = 'name',
    
class FacultyAdmin(admin.ModelAdmin):
    
    inlines = DepartmentInline,
    fields = 'name',

class DepartmentAdmin(admin.ModelAdmin):
    extra = 1
    inlines = GroupInline
    fields = 'name',


class VusesAdmin(admin.ModelAdmin):
    inlines = [FacultyInline]

    

admin.site.register(vuses, VusesAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department)

