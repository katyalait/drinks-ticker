from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from .models import Price

class ScatterLineChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, **kwargs):
        time_set = ['2018-11-14T21:00:00', '2018-11-14T21:20:00', '2018-11-14T21:40:00', '2018-11-14T22:00:00', '2018-11-14T22:20:00', '2018-11-14T22:40:00', '2018-11-14T23:00:00']
        interval = 5
        fosters = []
        g_and_t = []
        captain_morgan = []
        pampero = []
        roe_and_co = []
        zaconey = []
        vodka_redbull = []
        prices = Price.objects.all()
        for price in prices:
            if price.interval_index < interval:
                fosters.append({'y' : price.foster, 'x': time_set[int(price.interval_index-1)] })
                g_and_t.append({'y' : price.g_t, 'x': time_set[int(price.interval_index-1)]})
                captain_morgan.append({'y' : price.captain_morgan, 'x': time_set[int(price.interval_index-1)]})
                pampero.append({'y' : price.pampero, 'x': time_set[int(price.interval_index-1)]})
                roe_and_co.append({'y' : price.roe_and_co, 'x': time_set[int(price.interval_index-1)]})
                zaconey.append({'y' : price.zaconey, 'x': time_set[int(price.interval_index-1)]})
                vodka_redbull.append({'y' : price.vodka_redbull, 'x': time_set[int(price.interval_index-1)]})


        return [
            DataSet(type='line',
                    label='Fosters',
                    borderColor = 'blue',
                    data=fosters),
            DataSet(type='line',
                    label='Gin and Tonic',
                    borderColor='red',
                    data=g_and_t),
            DataSet(type='line',
                    label='Captain Morgan Splash',
                    borderColor='orange',
                    data=captain_morgan),
            DataSet(type='line',
                    label='Pampero Especial',
                    borderColor='green',
                    data=pampero),

            DataSet(type='line',
                    label='Roe & Co and Ginger Ale',
                    borderColor='yellow',
                    data=roe_and_co),
            DataSet(type='line',
                    label='Zaconey & Splash',
                    borderColor='purple',
                    data=zaconey),
            DataSet(type='line',
                    label='Double Vodka Redbull',
                    borderColor='pink',
                    data=vodka_redbull)

        ]
