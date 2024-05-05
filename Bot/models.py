from django.db import models
import datetime 

class Employee(models.Model):
    employee_id = models.CharField(max_length=100, default='')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='Doe')
    email = models.EmailField()
    departamento = models.CharField(max_length=100, default='Doe')
    puesto = models.CharField(max_length=100, default='Doe')
    dias_de_vacaciones_disponibles = models.IntegerField(default=0)
    # Agrega más campos según necesites
    # Otros campos como dirección, teléfono, etc.

    class Meta:
        app_label = 'Bot'



class Vacaciones(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dias_de_vacaciones = models.CharField(max_length=100, default='')
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
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_pago =  fecha_pago = models.DateField(null=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonificaciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    otros_ingresos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salud = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pension = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    otros_descuentos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salario_neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Beneficio(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tipo_beneficio = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Agrega más campos relacionados con los beneficios


    