from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import EventForm
from .models import Evento


def eventos(request):
    eventos_actuales = []
    eventos_pasados = []
    today = timezone.now()
    
    eventos = Evento.objects.all().order_by('-date_start')      #[:8] at end for last 8 records
    for record in eventos:
        if record.date_end > today:
            eventos_actuales.append(record)
        else:
            eventos_pasados.append(record)

    mess = "Lo sentimos pero en el momento no tenemos eventos"

    context = {'title': 'Eventos', 'eventos_actuales':eventos_actuales, 'eventos_pasados':eventos_pasados, 'mess':mess}
    return render(request, 'eventos/eventos.html', context)


def crearEvento(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('eventos')
    else:
        form = EventForm()

    context = {'title': 'Crear Evento', 'form':form}
    return render(request, 'eventos/logs/crearEvento.html', context)


def eventDetail(request, pk):
    evento = get_object_or_404(Evento, id=pk)

    context = {'title': 'Detalle Evento', 'evento':evento}
    return render(request, 'eventos/eventDetail.html', context)