from django.db import models
import datetime 

class Employee(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='Doe')
    email = models.EmailField()
    departamento = models.CharField(max_length=100, default='Doe')
    puesto = models.CharField(max_length=100, default='Doe')
    # Agrega más campos según necesites
    # Otros campos como dirección, teléfono, etc.

    class Meta:
        app_label = 'Bot'



class Vacaciones(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(default=datetime.date.today)
    motivo = models.TextField()
    aprobada = models.BooleanField(default=False)
    # Agrega más campos según necesites

    class Meta:
        app_label = 'Bot'

class Policy(models.Model):
    # Modelo para almacenar políticas de la empresa
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        app_label = 'Bot'

# Otros modelos que puedas necesitar para integrar con sistemas existentes


class Nomina(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    # Agrega más campos relacionados con la nómina

class Beneficio(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tipo_beneficio = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Agrega más campos relacionados con los beneficios


