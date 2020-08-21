from PersonalFinance import PersonalFinance
import pandas as pd
import matplotlib.pyplot as plt
import random


def main():
    principal = 10000.00
    contribution = 1000.00
    years = 20
    rate_avg = .08
    rate_low = .06
    rate_high = .1

    sp_data = PersonalFinance.get_sp_annual_returns()
    sp_mean = sp_data.loc[:, "value"].mean()
    sp_std = sp_data.loc[:, "value"].std()
    print("S&P 500 mean: {}".format(sp_mean))
    print("S&P 500 standard deviation: {}".format(sp_std))


    print("You are starting with ${:.2f}, contributing ${:.2f} annually. Your average rate of return is {:.2%}".format(
        principal, contribution, rate_avg))

    data = [{"year": 0, "value_avg": principal,
             "value_low": principal,
             "value_high": principal,
             "value_rand": principal}, ]

    for year in range(1, years):
        future_value_avg = PersonalFinance.compound(principal, rate_avg, year, contribution)
        future_value_low = PersonalFinance.compound(principal, rate_low, year, contribution)
        future_value_high = PersonalFinance.compound(principal, rate_high, year, contribution)
        rand_rate = random.normalvariate(sp_mean, sp_std*.1)
        future_value_rand = PersonalFinance.compound(principal, rand_rate, year, contribution)

        print("After {} year(s), you will have ${:.2f} saved. (rand={})".format(year, future_value_avg, rand_rate))
        data.append({"year": year,
                     "value_avg": future_value_avg,
                     "value_low": future_value_low,
                     "value_high": future_value_high,
                     "value_rand": future_value_rand})

    df = pd.DataFrame(data)
    print(df)

    df.plot.line(x="year", y=["value_avg", "value_low", "value_high", "value_rand"])
    plt.show()


if __name__ == "__main__":
    main()
