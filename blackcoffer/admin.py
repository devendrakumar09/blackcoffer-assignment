from django.contrib import admin
from .models import Jsondatafile
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StudentResource(resources.ModelResource):
   class Meta:
      model = Jsondatafile
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource

admin.site.register(Jsondatafile,StudentAdmin)