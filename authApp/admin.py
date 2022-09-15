from django.contrib import admin
from .models.paciente import Paciente
from .models.perSalud import PersonalSalud
from .models.usuario import (Usuario)

admin.site.register(Paciente)
admin.site.register(PersonalSalud)
admin.site.register(Usuario)