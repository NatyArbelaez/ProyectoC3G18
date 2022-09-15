from django.db import models
from .usuario import Usuario
from .perSalud import PersonalSalud

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key= True)
    id_personalSalud = models.ForeignKey(PersonalSalud, related_name='paciente', on_delete=models.CASCADE)
    username = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    ciudad = models.CharField('ciudad', max_length=35)
    fecha_Nacimiento = models.DateField()
    direccion = models.CharField('direccion', max_length=35)


#importar al init
