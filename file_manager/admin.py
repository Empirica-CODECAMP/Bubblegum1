from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import File, ExcelFile, Dashboard, Inflation

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'description')
    search_fields = ('name', 'description')


@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'description')
    search_fields = ('name', 'description')
    
@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'description')
    search_fields = ('title', 'description')
    
    
@admin.register(Inflation)
class InflationAdmin(admin.ModelAdmin):
    list_display = ('year', 'bpmos_medical_inflation', 'general_inflation')
    search_fields = ('year',)
    ordering = ('-year',)