from django.db import models
from .paciente import Paciente
from django.db.models.deletion import CASCADE

class HistoriaClinica(models.Model):
    id_historia_clinica = models.AutoField('Id_HistoriaClinica',primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    sugerencias_cuidado = models.TextField()
    diagnostico = models.TextField()
    entorno = models.TextField()
    fecha_de_sugerencia = models.DateField()
    descripcion = models.TextField()
