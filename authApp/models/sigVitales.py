from django.db import models
from .paciente import Paciente
from django.db.models.deletion import CASCADE

class SignosVitales(models.Model):
    id_signos_vitales = models.AutoField('Id_signos',primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    oximetria = models.CharField('oximetria',max_length=50)
    frecuencia_respiratoria = models.CharField('frecuencia_respiratoria', max_length=50)
    frecuencia_cardiaca = models.CharField('frecuencia_cardiaca', max_length=50)
    temperatura = models.CharField('temperatura', max_length=50)
    glicemias = models.CharField('glicemia', max_length=50)
    presion_arterial = models.CharField('presion', max_length=50)
    fecha_hora = models.DateTimeField()