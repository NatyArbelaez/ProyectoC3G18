from authApp.models.hisClinica import HistoriaClinica
from rest_framework import serializers

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ('id_paciente', 'sugerencias_cuidado', 'diagnostico', 'entorno', 'fecha_de_sugerencia', 'descripcion')

#importar al init
#revisar cambios