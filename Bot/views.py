from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Vacaciones, Policy, Employee
from bot_engine.bot import process_request
from django.db.models import F
from django.utils.dateparse import parse_date 
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

def company_info(request):
    return render(request, 'company_info.html')

def inicio(request):
    return render(request, 'home.html')

def nominasbeneficios(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        nueva_nomina = Nomina(
            empleado_id=employee_id,
            fecha_inicio=start_date,
            fecha_fin=end_date
        )
        nueva_nomina.save()

        messages.success(request, 'La solicitud de nómina ha sido enviada.')
        return redirect('nominasbeneficios')

    else:
        empleados = Employee.objects.all()
        return render(request, 'nominasbeneficios.html', {'empleados': empleados})

def personal(request):
    if request.method == 'POST':
        # Procesar el formulario y guardar los datos
        pass
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
