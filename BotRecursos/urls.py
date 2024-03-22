from django.urls import path
from django.contrib import admin
from Bot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('company_info/', views.company_info, name='company_info'),
    path('inicio/', views.inicio, name='inicio'),
    path('nominasbeneficios/', views.nominasbeneficios, name='nominasbeneficios'),
    path('personal/', views.personal, name='personal'),
    path('politicas/', views.politicas, name='politicas'),
    path('vacaciones/', views.vacaciones_view, name='vacaciones'),
    path('bot/', views.bot_view, name='bot_view'),
]

