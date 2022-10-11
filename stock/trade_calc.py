"""
Function to calculate value of tradein requests
"""

import datetime
from django.shortcuts import get_object_or_404
from .models import Maker


def calc_tradein(manu, year, odo, condition):
    """
     Function to calculate value of tradein requests

     Parameters:
     manu: string, manufacturer
     year: string, year of manufacturer
     odo: string, kilometers on odometer
     condition: string, condition of vehicle

     Returns: trade_value, int
    """
    base = get_object_or_404(Maker, maker=manu)
    base = base.base_price
    current_year = datetime.datetime.now()

    year_car = datetime.datetime.strptime(str(year), '%Y')
    days_diff = (current_year - year_car)
    year_diff = round((days_diff.days/365), 1)

    trade_value = int(base) * (1 - ((int(year_diff)/100 * 5.5) +
                                    ((int(odo)/10000)/100*6)))
    if trade_value <= 0:
        trade_value = 0

    condition_adjustment = trade_value/100 * 5
    if condition == '1':
        trade_value -= condition_adjustment
    elif condition == '3':
        trade_value += condition_adjustment

    return round(trade_value), round(trade_value * 1.5)
