# consumables/views.py
from django.http import JsonResponse
from .models import Consumable
from django.views.decorators.csrf import csrf_exempt

def calendar_events(request):
    events = []
    for item in Consumable.objects.all():
        events.append({
            "title": item.name,
        })
    return JsonResponse(events, safe=False)from django.shortcuts import render

# Create your views here.
