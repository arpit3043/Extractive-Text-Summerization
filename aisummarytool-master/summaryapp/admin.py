from django.contrib import admin
from summaryapp.models import Summary, ProcedureType, PatientGroup, DiseaseType, DeviceType, TypeOfStudy

admin.site.register(Summary)
admin.site.register(TypeOfStudy)
admin.site.register(DeviceType)
admin.site.register(DiseaseType)
admin.site.register(PatientGroup)
admin.site.register(ProcedureType)


