from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from eventos.models import Evento

def main(request):
    eventos_actuales = []
    eventos_pasados = []
    eventos = []
    
    eventos = Evento.objects.all().order_by('-date_start')      #[:8] at end for last 8 records
    today = timezone.now()
    for record in eventos:
        if record.date_end > today:
            eventos_actuales.append(record)
        else:
            eventos_pasados.append(record)
        
        if eventos_actuales:
            eventos = eventos_actuales
            mess = 0
        else:
            eventos = eventos_pasados
            
    mess = "Lo sentimos pero en el momento no tenemos eventos pendientes"
    
    context = {'title': 'Python Colombia', 'eventos':eventos, 'mess':mess}
    return render(request, 'pycol/main.html', context)


def conducta(request):
    
    context = {'title': 'Codigo de Conducta'}
    return render(request, 'pycol/conducta.html', context)


def privacy(request):
    
    context = {'title': 'Poliza de Privacidad'}
    return render(request, 'pycol/privacy.html', context)


def page401(request):

    context = {'title': 'Poliza de Privacidad'}
    return render(request, 'pycol/status_codes/page401.html', context)
    