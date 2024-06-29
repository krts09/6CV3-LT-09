from django.contrib import admin
from TESCOM_MAIN.models import *

# Register your models here.

@admin.register(HorarioDisponible)
class HorarioDisponibleAdmin(admin.ModelAdmin):
    # list_display = ('profesor', 'dia_semana', 'horario_inicio', 'horario_fin')
    #search_fields = ('profesor',)
    pass


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    pass


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass


@admin.register(TrabajoTerminal)
class TrabajoTerminalAdmin(admin.ModelAdmin):
    pass


@admin.register(AlumnoTrabajoTerminal)
class AlumnoTrabajoTerminalAdmin(admin.ModelAdmin):
    pass


@admin.register(Observaciones)
class ObservacionesAdmin(admin.ModelAdmin):
    pass
