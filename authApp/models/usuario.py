from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.deletion import CASCADE

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        
        if not username:
            raise ValueError('Los usuarios deben tener un nombre de usuario')
        user = self.model(username=username)
        user.self_password(password)
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(primary_key=True, max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256) #el nombre dentro del parentesis debe ser igal al de la tabla?
    rolPerfil = models.CharField('RolPerfil', max_length = 35) #paciente, perSalud, familiar, auxSalud
    nombre = models.CharField('Nombre', max_length = 35)
    apellidos = models.CharField('Apellidos', max_length = 35)
    telefono = models.CharField('Telefono', max_length = 35)
    genero = models.CharField('Genero', max_length = 35)

    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'


#importar al init