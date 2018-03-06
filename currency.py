# -*- coding: utf-8 -*-


import datetime
import pandas as pd


class Currency:
    """
    A general currency with exchange rate to CNY available.
    """
    def __init__(self, name, exchangerate_factory=None):
        self.name = name
        self.factory = exchangerate_factory

    def __str__(self):
        return self.name.upper()

    def me2cny(self, day=datetime.date.today()):
        """
        Return exchange rate from me to CNY.
        """
        if self.factory:
            rates = self.factory.get_exchangerate()
            if day in rates.index:
                return rates.loc[day, 'Rate']
            else:
                day_stamp = pd.Timestamp(day)
                if day_stamp > rates.index[0]:
                    return rates.loc[:day].iloc[-1]['Rate']
                else:
                    raise KeyError(f'No exchange rate found on {day}')
        else:
            return 1


class FileExchangeRate:
    """
    One object that produce exchange reate data from csv file.
    """
    def __init__(self, filepath):
        self.csvfile = filepath
        
    def get_exchangerate():
        """
        Return exchange rates from csv file.
        """
        return pd.read_csv(self.csvfile, parse_dates=['Date'], index_col=0)
