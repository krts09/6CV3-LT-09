<<<<<<< Updated upstream
from django.shortcuts import render
from datetime import date, datetime
from django.views.generic import ListView
from .models import Agenda
from .forms import FechaForm

=======
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .forms import TrabajoTerminalForm
from .models import Alumno, TrabajoTerminal, AlumnoTrabajoTerminal
>>>>>>> Stashed changes

# Create your views here.

def success(request):
    return render(request, 'success.html')


def login_alumno(request):
    return render(request, "login.html")


def forgot_password(request):
    return render(request, "forgot-password.html")


def up_protocol(request):
<<<<<<< Updated upstream
    return render(request, "up-protocol.html")

class AgendaGeneralListView(ListView):
    model = Agenda
    paginate_by = 100
    template_name = 'agendas/agenda_general/agenda_general.html'
    context_object_name = 'agendas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FechaForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = FechaForm(self.request.GET or None)
        if form.is_valid():
            fecha = form.cleaned_data.get('fecha')
            if fecha:
                return queryset.filter(fecha_separacion=fecha)
        return queryset.filter(fecha_separacion=date.today())
=======
    if request.method == 'POST':
        form = TrabajoTerminalForm(request.POST, request.FILES)
        alumno_id = request.POST.get('alumno_id')
        try:
            alumno = Alumno.objects.get(alumno_id=alumno_id)
        except Alumno.DoesNotExist:
            form.add_error('alumno_id', 'Numero de Boleta Incorrecto.')
            return render(request, 'up-protocol.html', {'form':form})

        if form.is_valid():
            trabajo_terminal = form.save(commit=False)
            trabajo_terminal.alumno = alumno
            trabajo_terminal.save()
            form.save_m2m()
            AlumnoTrabajoTerminal.objects.create(alumno_id=alumno, trabajo_terminal=trabajo_terminal)
            return redirect('success')
    else:
        form = TrabajoTerminalForm()
    return render(request, 'up-protocol.html', {'form': form})

>>>>>>> Stashed changes
