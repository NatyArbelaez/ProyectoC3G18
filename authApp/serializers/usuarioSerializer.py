from authApp.models.usuario import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'rolPerfil', 'nombre', 'apellidos', 'telefono', 'genero')


#importar al init