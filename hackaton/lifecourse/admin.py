from django.contrib import admin

from .models import Department, Group, Faculty, vuses

class GroupInline(admin.TabularInline):
    model = Group

class DepartmentInline(admin.StackedInline):
    model = Department



class FacultyInline(admin.StackedInline):
    model = Faculty

    
class FacultyAdmin(admin.ModelAdmin):
    
    inlines = DepartmentInline,
    fields = 'name',

class DepartmentAdmin(admin.ModelAdmin):
    inlines = GroupInline,
    fields = 'name',


class VusesAdmin(admin.ModelAdmin):
    inlines = [FacultyInline]
    fields = 'name',
    

##admin.site.register(Faculty, FacultyAdmin)
##admin.site.register(Department, DepartmentAdmin)
##admin.site.register(Group)
admin.site.register(vuses, VusesAdmin)

