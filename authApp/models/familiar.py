from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from .usuario import Usuario
from .paciente import Paciente

class Familiar(models.Model):
    id_familiar = models.AutoField('Id_Familiar',primary_key=True)
    username = models.ForeignKey(Usuario, on_delete=models.CASCADE)   
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    parentesco = models.CharField('Parentesco', max_length = 100)
    correo = models.EmailField('Email', max_length = 100)