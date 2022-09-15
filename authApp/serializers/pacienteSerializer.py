from authApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id_personalSalud', 'username', 'ciudad', 'fecha_Nacimiento', 'direccion')

#importar al init