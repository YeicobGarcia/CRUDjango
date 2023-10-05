from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} {{1}}"
        return texto.format(self.nombre, self.creditos)
    
class Usuarios(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=25)
    telefono = models.IntegerField(null=True)
    f_nacimiento = models.DateField(null=True)
    f_registro = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'usuarios'