from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class poorvika_price(ImportExportModelAdmin):

    class Meta:
        model =Poorvika()
        Field = ('id',)


admin.site.register(Poorvika, poorvika_price)


class home_appliance(ImportExportModelAdmin):

    class Meta:
        model =HomeApplainces()
        Field = ('id',)


admin.site.register(HomeApplainces, home_appliance)
