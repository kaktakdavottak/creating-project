from django.contrib import admin

from .models import Table, CSVFile


class TableAdmin(admin.ModelAdmin):
    pass


class CSVFileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Table, TableAdmin)
admin.site.register(CSVFile, CSVFileAdmin)
