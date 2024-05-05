from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Vacaciones, Policy, Employee
from bot_engine.bot import process_request
from django.db.models import F
from django.utils.dateparse import parse_date 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Nomina

def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

def company_info(request):
    return render(request, 'company_info.html')

def inicio(request):
    return render(request, 'home.html')


def politicas(request):
    return render(request, 'politicas.html')
    
def bot_view(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')
        response = process_request(question)
        return JsonResponse({'response': response['answer'], 'redirect_url': response['redirect_url']})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def vacaciones_view(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('employee_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Verificar si el número de empleado está vacío
        if not empleado_id:
            messages.error(request, 'El número de empleado no puede estar vacío.')
            return redirect('vacaciones')

        # Verificar si las fechas de inicio y fin están vacías
        if not start_date or not end_date:
            messages.error(request, 'Debes proporcionar las fechas de inicio y fin.')
            return redirect('vacaciones')

        try:
            employee = Employee.objects.get(employee_id=empleado_id)
            messages.success(request, f'Hola {employee.nombre}')
        except Employee.DoesNotExist:
            messages.error(request, 'El número de empleado es incorrecto.')
            return redirect('vacaciones')

        try:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
        except (TypeError, ValueError):
            raise ValidationError(_('Invalid date format. Use YYYY-MM-DD.'), code='invalid')

        # Calcular la duración de la solicitud en días
        duration = (end_date - start_date).days + 1

        # Verificar si el empleado tiene suficientes días de vacaciones disponibles
        if employee.dias_de_vacaciones_disponibles >= duration:
            aprobada = True
            employee.dias_de_vacaciones_disponibles -= duration
            employee.save()
        else:
            aprobada = False

        nueva_solicitud = Vacaciones(
            employee=employee,
            dias_de_vacaciones=duration,
            fecha_inicio=start_date,
            fecha_fin=end_date,
            aprobada=aprobada
        )
        nueva_solicitud.save()

        if aprobada:
            messages.success(request, f'La solicitud de vacaciones por {duration} días ha sido aprobada.')
        else:
            messages.error(request, f'La solicitud de vacaciones por {duration} días ha sido denegada debido a la falta de días disponibles.')

        return redirect('vacaciones')

    else:
        todas_vacaciones = Vacaciones.objects.all()
        return render(request, 'vacaciones.html', {'vacaciones': todas_vacaciones})

def personal(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('employee_id')

        # Verificar si el número de empleado está vacío
        if not empleado_id:
            messages.error(request, 'El número de empleado no puede estar vacío.')
            return redirect('personal')

        try:
            employee = Employee.objects.get(employee_id=empleado_id)
            messages.success(request, f'Empleado encontrado: {employee.nombre} {employee.apellido}')
        except Employee.DoesNotExist:
            messages.error(request, 'El número de empleado es incorrecto.')
            return redirect('personal')

        # Actualizar los datos del empleado si se proporcionaron nuevos valores
        new_name = request.POST.get('new_name')
        new_email = request.POST.get('new_email')
        new_departamento = request.POST.get('new_departamento')
        new_puesto = request.POST.get('new_puesto')
        new_apellido = request.POST.get('new_apellido')

        if new_name:
            employee.nombre = new_name
        if new_email:
            employee.email = new_email
        if new_departamento:
            employee.departamento = new_departamento
        if new_puesto:
            employee.puesto = new_puesto
        if new_apellido:
            employee.apellido = new_apellido

        employee.save()

        # Pasar los datos del empleado a la plantilla
        return render(request, 'personal.html', {'user': employee})

    else:
        # Pasar un objeto vacío a la plantilla
        employee = {
            'nombre': '',
            'apellido': '',
            'email': '',
            'departamento': '',
            'puesto': ''
        }
        return render(request, 'personal.html', {'user': employee})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee, Nomina

def nominasbeneficios(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('employee_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if not all([empleado_id, start_date, end_date]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('nominasbeneficios')

        try:
            employee = Employee.objects.get(employee_id=empleado_id)
            messages.success(request, f'Empleado encontrado: {employee.nombre} {employee.apellido}')
        except Employee.DoesNotExist:
            messages.error(request, 'El número de empleado es incorrecto.')
            return redirect('nominasbeneficios')

        nueva_nomina = Nomina(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
        )
        nueva_nomina.save()

        messages.success(request, 'La nómina ha sido enviada correctamente al correo electrónico del empleado.')
        return redirect('nominasbeneficios')

    else:
        empleados = Employee.objects.all()
        return render(request, 'nominasbeneficios.html', {'empleados': empleados})
