from django.shortcuts import render
from django.http import HttpResponse
from jchart import Chart
from .models import Price

def index(request):
    return render(request, 'main/index.html')
