from django.contrib import admin
from .models import Employee, Vacaciones, Policy, Nomina, Beneficio

admin.site.register(Employee)
admin.site.register(Vacaciones)
admin.site.register(Policy)
admin.site.register(Nomina)
admin.site.register(Beneficio)

