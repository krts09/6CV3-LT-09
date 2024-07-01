from django.shortcuts import render
from datetime import date, datetime
from django.views.generic import ListView
from .models import Agenda
from .forms import FechaForm


# Create your views here.


def login_alumno(request):
    return render(request, "login.html")


def forgot_password(request):
    return render(request, "forgot-password.html")


def up_protocol(request):
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