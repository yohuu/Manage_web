from django.contrib import admin

# Register your models here.

from indis.models import Student,Project,Module

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'deadline', 'progress', 'budget', 'description', 'leader')
    search_fields = ['name']      # 在 "name" 字段中查找项目 
    date_hierarchy = 'start_date' # 以开始日期为导航
    list_filter = ['start_date']  # 过滤器
    fieldsets = [                 # 设置编辑模块样式
        (None,               {'fields': ['name']}),
        ('Date Information', {'fields': ['start_date','deadline'], 'classes': ['wide']}),
        ('Other Information', {'fields': ['progress','budget','leader'], 'classes': ['wide']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [ModuleInline]     # 关联ModuleInline行


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'birthday')
    search_fields = ['name']      # 在 "name" 字段中查找项目 
    list_filter = ['birthday']    # 过滤器
    fieldsets = [                 # 设置编辑模块样式
        (None,               {'fields': ['name']}),
        ('Information', {'fields': ['sex','birthday'], 'classes': ['wide']}),
    ]
    inlines = [ProjectInline,ModuleInline]     # 关联ModuleInline和ProjectInline行

admin.site.register(Project, ProjectAdmin)     # 注册ProjectAdmin

admin.site.register(Student, StudentAdmin)     # 注册StudentAdmin