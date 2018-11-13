from django.shortcuts import render
from django.http import HttpResponse
from jchart import Chart
from .models import Price
from datetime import datetime
import time
from . import charts
from . import views
from jchart.views import ChartView

def index(request):
    hour= 21
    minute=00
    interval = 0
    time_set = [{'hour': 21, 'minute': 00}, {'hour': 21, 'minute': 20}, {'hour': 21, 'minute': 40}, {'hour': 22, 'minute': 00}, {'hour': 22, 'minute': 20}, {'hour': 22, 'minute': 40}, {'hour': 23, 'minute': 00}]
    localtime = time.localtime(time.time())
    current_hour = localtime.tm_hour
    current_minute = localtime.tm_min
    if (current_hour> hour or current_minute>minute):
        if (interval+1< 10):
            next_time = time_set[interval+1]
            if next_time['hour']==localtime.tm_hour and localtime.tm_min==next_time['minute']:
                interval = interval+1

    ChartView.from_chart(charts.ScatterLineChart())
    return render(request, 'main/index.html', {'interval': interval})

    
