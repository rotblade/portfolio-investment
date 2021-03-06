# -*- coding: utf-8 -*-
"""
This module define Currency related objects.
"""


import datetime
import pandas as pd


class Currency:
    """
    A general currency with exchange rate to CNY available.
    """
    def __init__(self, name, rate_source=None):
        self.name = name
        self.rate_factory = rate_source

    def __str__(self):
        return self.name.upper()

    def me2cny(self, t=datetime.date.today()):
        """
        Return exchange rate from me to CNY.
        """
        rate = 1.0
        if self.rate_factory:
            rate = self.rate_factory.get(t)

        return rate


class FileExchangeRate:
    """
    One object that produce exchange reate data from csv file.
    """
    def __init__(self, filepath):
        self.csvfile = filepath

    def get(self, t):
        """
        Return exchange rates in specified time.
        """
        rates = pd.read_csv(self.csvfile, parse_dates=[0], index_col=0)
        if t in rates.index:
            return rates.loc[t][0]
        else:
            t_stamp = pd.Timestamp(t)
            if t_stamp > rates.index[0]:
                return rates.loc[:t].iloc[-1][0]
            else:
                raise KeyError(f'No exchange rate found on {t}')
