from authApp.models.perSalud import PersonalSalud

from rest_framework import serializers

class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSalud
        fields = ('username', 'rol', 'especialidad')

#importar al init