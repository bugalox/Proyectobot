# Generated by Django 5.0.3 on 2024-05-05 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0012_nomina_pago'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomina',
            old_name='pago',
            new_name='bonificaciones',
        ),
        migrations.AddField(
            model_name='nomina',
            name='deducciones',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='horas_extra',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='otros_descuentos',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='otros_ingresos',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='pension',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='salario_base',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='salario_neto',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='salud',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='total_descuentos',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='total_devengado',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='nomina',
            name='total_ingresos',
            field=models.CharField(default='', max_length=100),
        ),
    ]
