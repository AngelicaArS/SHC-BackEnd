from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 100)
    apellidos = models.CharField('Apellidos', max_length = 100)
    documento = models.CharField('Documento', max_length = 100)
    direccion = models.CharField('Direccion', max_length = 100)
    telefono = models.CharField('Telefono', max_length = 100)
    genero = models.CharField('Genero', max_length = 100)
    fecha_nacimiento = models.CharField('FechaNacimiento', max_length = 100)
    contrasena = models.CharField('Contrasena', max_length = 256)
    correo = models.EmailField('Correo', max_length = 100)
    fecha_registro = models.CharField('FechaRegistro', max_length = 100)
    id_tipo_usuario = models.IntegerField('id_tipo_usuario', max_length = 4)    

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'