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
    time_set = [{'hour': 21, 'minute': 00}, {'hour': 21, 'minute': 20}, {'hour': 21, 'minute': 35}, {'hour': 22, 'minute': 00}, {'hour': 22, 'minute': 20}, {'hour': 22, 'minute': 40}, {'hour': 23, 'minute': 00}]
    prices = [PriceStatic(5.80, 9.20, 8.40, 15.80, 9.20, 16.00, 19.80, 0), PriceStatic(2.50, 9.00, 8.40, 10.00, 6.00, 10.00, 19.80, 1),
    PriceStatic(5.80, 6.00, 8.40, 10.00, 6.00, 16.00, 19.80, 2), PriceStatic(2.50, 6.00, 8.40, 15.80, 9.20, 16.00, 10.00, 3),
    PriceStatic(5.80, 9.20, 5.00, 10.00, 9.20, 10.00, 10.00, 4), PriceStatic(2.50, 9.20, 5.00, 10.00, 6.00, 16.00, 19.80, 5),
    PriceStatic(2.50, 6.00, 8.40, 15.80, 6.00, 10.00, 19.80, 6),PriceStatic(5.80, 9.20, 8.40, 15.80, 9.20, 10.00, 10.00, 7),
    PriceStatic(5.8, 6.00, 5.00, 10.00, 9.20, 16.00, 10.00, 8),PriceStatic(2.50, 9.20, 8.40, 10.00, 6.00, 16.00, 10.00, 9)]
    arrows = [{'name': 'Fosters (FRS)', 'img': 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg'},
    {'name': 'Tanqueray G&T (TGT)', 'img':'https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg'},
    {'name': 'Captain Morgan Splash (CMS)', 'img': 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg'},
    {'name': 'Double Especial & Tropical Red Bull (DETR)', 'img':'https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg' },
    {'name': 'Roe & Co + Ginger Ale (RCG)', 'img':'https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg'},
    {'name': 'Double Jagerbomb (DJG)', 'img':'https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg'},
    {'name': 'Double Vodka Redbull (VDKR)', 'img':'https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg'}]


    commentary = [Commentary('\"No way I’m buying anything but Fosters at this price\" – Michael O’R. -Mechanical Engineering',
    '\"I refuse to drink any more gin unless it’s in one of those fancy glasses\"- Gio Radaelli',
    '\"No going to leave it a while and see if it drops\" – Mark T.', 0), Commentary('\"Not much of a Fosters fan but at €2.50 beggars can’t be choosers\" – Peter S. Marketing',
    '\"€10 for a double Especial? That’s bloody trouble\" Christian Casey', '\"The queues are far too long\" -Mark F', 1),
    Commentary('\"No more spirits for me, I’ve got a 9am\" – Conor C.', '\"Vodka has made me the influencer I am today, I drank it before I scored the funniest try EVER\"- Rob Lipsett',
    '\"I rest my case; the boom is back\" – Michael R', 2), Commentary('\n"Its expensive so this Double Vodka is the last one I’m going to get\" – Vanessa G.',
    '\"I can only drink shots\" – Becca S', '\"This night has been pivotal in the squads preparation for the world cup next year, massive thanks toDIT I&E society\" – Joe Schmidt', 3),
    Commentary('\"At this price it doesn’t make sense, I’ll be buying Captain Morgan\" – Laura D.', '\"The Queues have slowing down so I reckon it’ll fall heavily soon\" – Danny M.',
    '\"Can’t believe I got caught at the bar during the price change\" – Peter K. – Business & Management', 4), Commentary('\"Comparatively, Fosters is the best value on the market right now\" -Lucy K. – Business & Spanish',
    '\"I’m meant to be doing dry November\" -Ciara L.', '\"Yeah definitely loading up on Captain Morgans while it’s cheap\" – Lorcan M.', 5),
    Commentary('\"Man, Roe & Co gets you fairly buzzed.\" Roy Keane', '\"Everyone’s doing bombs and I don’t want to miss out\" – Sarah F.', '\n"Its expensive so this is the last one I’m going to get\" – Vanessa G.', 6),
    Commentary('\"Won’t be going near Fosters, be sticking with the Double Vodka RedBull’s now\" – Katie L. Engineering', '\"I’m more of a Whiskey man myself\" – Rob Kearney',
    '\"Not even sure what this Tropical stuff is but it’s good\"- Leo Varadkar', 7), Commentary('\"Roe and Co is good, but its not THAT good\" – Rachel O’R.', '\"I Love Vodka #Gymshark\"- Sian Walton', '\"I can’t fork that out for Jager\" – Peter D.', 8),
    Commentary('\"Ah at this price you can’t beat a Double Especial Tropical\" – Michael R.', '\"I have too many shots, need to go back to the beer\" – Jamie R.', '\"Huge queues for Fosters leading to frantic buying\" – DIT SMF analyst', 9)]
    current_commentary = commentary[0]
    localtime = time.localtime(time.time())
    current_hour = localtime.tm_hour
    current_minute = localtime.tm_min
    current_time = time_set[interval]
    for curtime in time_set:
        if current_hour>= curtime['hour'] and current_minute>curtime['minute']:
            interval = time_set.index(curtime)
            previous_prices = prices[interval-1]
            current_prices = prices[interval]
            index = 0
            for statement in arrows:
                if previous_prices.list[index]<current_prices.list[index]:
                    statement['img']='https://upload.wikimedia.org/wikipedia/commons/7/7f/Green_equilateral_triangle_point_up.svg'
                elif previous_prices.list[index]>current_prices.list[index]:
                    statement['img']='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Red_Triangle.svg/1200px-Red_Triangle.svg.png'
                else:
                    statement=statement
                index = index+1
    current_commentary = commentary[interval]



    ChartView.from_chart(charts.ScatterLineChart())
    return render(request, 'main/index.html', {'interval': interval, 'prices': prices[interval], 'arrows': arrows, 'commentary': current_commentary})


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
        self.list = [self.foster,self.g_t,
        self.captain_morgan,
        self.pampero,
        self.roe_and_co,
        self.jaegerbomb,
        self.vodka_redbull,
        self.interval_index ]

class Commentary:
    def __init__(self, comment1, comment2, comment3, interval):
        self.comment1 = comment1
        self.comment2 = comment2
        self.comment3 = comment3
        self.interval = interval
