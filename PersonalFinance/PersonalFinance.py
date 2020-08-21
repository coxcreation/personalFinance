import os
import pandas as pd


class PersonalFinance:
    def __init__(self):
        pass

    @staticmethod
    def compound(p, r, y, c):
        """
        p = Principal
        r = annual interest rate
        y = years of compounding
        c = annual contribution

        Balance(y) = p(1+r)^y + c[((1+r)^(y+1)-(1+r))/r]
        """
        return p * pow((1 + r), y) + c * ((pow((1 + r), (y + 1)) - (1+r)) / r)

    @staticmethod
    def get_sp_annual_returns():
        df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/sp-500-historical-annual-returns.csv")
        return df
