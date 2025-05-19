from django.db import models

# Create your models here.
class Carrera(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{0} -> {1}".format(self.clave, self.nombre)

class Plan(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.clave, self.nombre)

class Materia(models.Model):
    # Estos son sus atributos
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    creditos = models.IntegerField(default=5)
    estatus = models.BooleanField(default=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)

    # Estos son sus métodos
    def __str__(self):
        return "{0} - {1}".format(self.clave, self.nombre)