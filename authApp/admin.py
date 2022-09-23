from django.contrib import admin
from .models.paciente import Paciente
from .models.perSalud import PersonalSalud
from .models.usuario import Usuario
from .models.familiar import Familiar
from .models.hisClinica import HistoriaClinica
from .models.sigVitales import SignosVitales

admin.site.register(Paciente)
admin.site.register(PersonalSalud)
admin.site.register(Usuario)
admin.site.register(Familiar)
admin.site.register(HistoriaClinica)
admin.site.register(SignosVitales)