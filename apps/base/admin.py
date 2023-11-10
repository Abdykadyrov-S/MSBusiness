from django.contrib import admin
from .models import Settings, Contact, About, OperationProcess, Service_Contact

admin.site.register(Settings)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(OperationProcess)
admin.site.register(Service_Contact)


