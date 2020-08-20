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
