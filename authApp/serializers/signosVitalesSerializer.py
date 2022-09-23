from authApp.models.sigVitales import SignosVitales
from rest_framework import serializers

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ('id_paciente', 'oximetria', 'frecuencia_respiratoria', 'frecuencia_cardiaca', 'temperatura', 'glicemias', 'presion_arterial', 'fecha_hora')

#importar al init
#revisar cambios