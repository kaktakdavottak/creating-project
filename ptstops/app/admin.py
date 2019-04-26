from django.contrib import admin
from .models import Route, Station


class RouteAdmin(admin.ModelAdmin):
    pass


class StationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Route, RouteAdmin)
admin.site.register(Station, StationAdmin)

