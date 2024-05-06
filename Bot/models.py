from django.db import models
from datetime import datetime
from .observer import Subject

# Clase base PolicyDecorator
class PolicyDecorator:
    def __init__(self, policy):
        self._policy = policy

    def get_info(self):
        return self._policy.get_info()

class HtmlPolicyDecorator(PolicyDecorator):
    def get_info(self):
        return f'<html><body>{super().get_info()}</body></html>'

class HeaderPolicyDecorator(PolicyDecorator):
    def get_info(self):
        return f'POLÍTICA: {super().get_info()}'

class FooterPolicyDecorator(PolicyDecorator):
    def get_info(self):
        return f'{super().get_info()}<br><br>Este es el pie de página.'

class TimestampPolicyDecorator(PolicyDecorator):
    def get_info(self):
        return f'{super().get_info()}<br><br>Última actualización: {datetime.now()}'

class Policy(Subject, models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated = models.DateTimeField(default=datetime.now)

    def update_policy(self, new_content):
        self.content = new_content
        self.last_updated = datetime.now()
        self.notify(content=new_content, last_updated=self.last_updated)

    class Meta:
        app_label = 'Bot'

class Employee(models.Model):
    employee_id = models.CharField(max_length=100, default='')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='Doe')
    email = models.EmailField()
    departamento = models.CharField(max_length=100, default='Doe')
    puesto = models.CharField(max_length=100, default='Doe')
    dias_de_vacaciones_disponibles = models.IntegerField(default=0)
    policies_subscribed = models.ManyToManyField(Policy, related_name='subscribers', blank=True)

    class Meta:
        app_label = 'Bot'

class Vacaciones(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dias_de_vacaciones = models.CharField(max_length=100, default='')
    fecha_inicio = models.DateField(default=datetime.now)
    fecha_fin = models.DateField(default=datetime.now)
    motivo = models.TextField()
    aprobada = models.BooleanField(default=False)
    # Agrega más campos según necesites

    class Meta:
        app_label = 'Bot'

class Nomina(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_pago = models.DateField(null=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonificaciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    otros_ingresos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salud = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pension = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    otros_descuentos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salario_neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        app_label = 'Bot'

class Beneficio(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tipo_beneficio = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Agrega más campos relacionados con los beneficios


    