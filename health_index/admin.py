# from django.contrib import admin
# from import_export.admin import ExportMixin
# from import_export.admin import ImportExportModelAdmin
# from import_export import resources
# from .models import HealthIndexRawData

# class HealthIndexResource(resources.ModelResource):
#     class Meta:
#         model = HealthIndexRawData

# @admin.register(HealthIndexRawData)
# class HealthIndexAdmin(ExportMixin, admin.ModelAdmin):
#     resource_class = HealthIndexResource
#     list_display = ('year', 'no_nurses', 'no_doctors', 'hospital_beds', 'infant_mortality', 'life_expectancy', 'tb_incidence')
#     search_fields = ('year',)
#     list_filter = ('year',)



from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import HealthIndexRawData

class HealthIndexResource(resources.ModelResource):
    class Meta:
        model = HealthIndexRawData

@admin.register(HealthIndexRawData)
class HealthIndexAdmin(ImportExportModelAdmin):
    resource_class = HealthIndexResource
    list_display = ('year', 'no_nurses', 'no_doctors', 'hospital_beds', 'infant_mortality', 'life_expectancy', 'tb_incidence')
    search_fields = ('year',)
    list_filter = ('year',)
