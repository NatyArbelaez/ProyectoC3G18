from django.db import models
from .usuario import Usuario

class PersonalSalud(models.Model):
    id_personalSalud = models.AutoField(primary_key=True)
    username = models.ForeignKey(Usuario, related_name= 'perSalud', on_delete=models.CASCADE)
    rol = models.CharField('rol', max_length=35) #medico o enfermero
    especialidad = models.CharField('especialidad', max_length=35)


#importar al init