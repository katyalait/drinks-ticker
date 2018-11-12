from django.urls import path
from django.urls import include
from django.conf.urls import url
from . import charts
from . import views
from jchart.views import ChartView

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^charts/scatter_line_chart/$',
        ChartView.from_chart(charts.ScatterLineChart()),
        name='scatter_line_chart')
]
