from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from .models import Price
import time

class ScatterLineChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, **kwargs):
        time_set = ['2018-11-14 21:00:00', '2018-11-14 21:20:00', '2018-11-14 21:40:00', '2018-11-14 22:00:00', '2018-11-14 22:20:00', '2018-11-14 22:40:00', '2018-11-14 23:00:00']
        interval = 5
        fosters = []
        g_and_t = []
        captain_morgan = []
        pampero = []
        roe_and_co = []
        jaegerbomb = []
        vodka_redbull = []
        prices = [PriceStatic(5.80, 9.20, 8.40, 15.80, 9.20, 16.00, 19.80, 0), PriceStatic(2.50, 9.00, 8.40, 10.00, 6.00, 10.00, 19.80, 1),
        PriceStatic(5.80, 6.00, 8.40, 10.00, 6.00, 16.00, 19.80, 2), PriceStatic(2.50, 6.00, 8.40, 15.80, 9.20, 16.00, 10.00, 3),
        PriceStatic(5.80, 9.20, 5.00, 10.00, 9.20, 10.00, 10.00, 4), PriceStatic(2.50, 9.20, 5.00, 10.00, 6.00, 16.00, 19.80, 5),
        PriceStatic(2.50, 6.00, 8.40, 15.80, 6.00, 10.00, 19.80, 6),PriceStatic(5.80, 9.20, 8.40, 15.80, 9.20, 10.00, 10.00, 7),
        PriceStatic(5.8, 6.00, 5.00, 10.00, 9.20, 16.00, 10.00, 8),PriceStatic(2.50, 9.20, 8.40, 10.00, 6.00, 16.00, 10.00, 9)]

        hour= 21
        minute=00
        interval = 0
        max_interval = 9
        time_set2 = [{'hour': 21, 'minute': 00}, {'hour': 21, 'minute': 20}, {'hour': 21, 'minute': 40}, {'hour': 22, 'minute': 00}, {'hour': 22, 'minute': 20}, {'hour': 22, 'minute': 40}, {'hour': 23, 'minute': 00}]
        localtime = time.localtime(time.time())
        local_hour = localtime.tm_hour
        local_minute = localtime.tm_min

        current_time = time_set2[interval]
        if interval!=max_interval:
            next_time = time_set2[interval+1]
            if local_hour==next_time['hour'] and local_minute==next_time['minute']:
                interval = interval +1
        for price in prices:
            if price.interval_index==interval:
                fosters.append({'y' : price.foster, 'x': time_set[int(price.interval_index)] })
                g_and_t.append({'y' : price.g_t, 'x': time_set[int(price.interval_index)]})
                captain_morgan.append({'y' : price.captain_morgan, 'x': time_set[int(price.interval_index)]})
                pampero.append({'y' : price.pampero, 'x': time_set[int(price.interval_index)]})
                roe_and_co.append({'y' : price.roe_and_co, 'x': time_set[int(price.interval_index)]})
                jaegerbomb.append({'y' : price.jaegerbomb, 'x': time_set[int(price.interval_index)]})
                vodka_redbull.append({'y' : price.vodka_redbull, 'x': time_set[int(price.interval_index)]})


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
                    label='Double Jaeger-Bomb',
                    borderColor='purple',
                    data=jaegerbomb),
            DataSet(type='line',
                    label='Double Vodka Redbull',
                    borderColor='pink',
                    data=vodka_redbull)

        ]

class PriceStatic:
    def __init__(self, fosters, g_and_t, captain_morgan, pampero, roe_and_co, jaegerbomb, vodka_redbull, interval_index):
        self.foster = fosters
        self.g_t = g_and_t
        self.captain_morgan = captain_morgan
        self.pampero = pampero
        self.roe_and_co = roe_and_co
        self.jaegerbomb = jaegerbomb
        self.vodka_redbull = vodka_redbull
        self.interval_index = interval_index
