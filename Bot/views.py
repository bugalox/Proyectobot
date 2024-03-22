from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Vacaciones, Policy, Employee
from bot_engine.bot import process_request

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

def vacaciones_view(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('employee_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        nueva_solicitud = Vacaciones(
            employee_id=empleado_id,
            fecha_inicio=start_date,
            fecha_fin=end_date
        )
        nueva_solicitud.save()

        messages.success(request, 'La solicitud de vacaciones ha sido enviada.')
        return redirect('vacaciones')

    else:
        todas_vacaciones = Vacaciones.objects.all()
        return render(request, 'vacaciones.html', {'vacaciones': todas_vacaciones})

def bot_view(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')
        response = process_request(question)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)
