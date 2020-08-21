from PersonalFinance import PersonalFinance
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random
"""
This script is using functions from PersonalFinance to calculate investment returns with an annual contribution. The
random return is generated using historic statistical data for the S&P 500 to 'predict' possible future performance.
"""


def main():
    principal = 100000.00
    contribution = 19500.00
    years = 30
    rate_avg = .08
    rate_low = .06
    rate_high = .10

    sp_data = PersonalFinance.get_sp_annual_returns()
    sp_mean = sp_data.loc[:, "value"].mean()
    sp_std = sp_data.loc[:, "value"].std()
    print("S&P 500 mean: {}".format(sp_mean))
    print("S&P 500 standard deviation: {}".format(sp_std))


    print("You are starting with ${:.2f}, contributing ${:.2f} annually. Your average rate of return is {:.2%}".format(
        principal, contribution, rate_avg))

    data = [{"year": 0, "Average Return": principal,
             "Low Return": principal,
             "High Return": principal,
             "Random Return": principal}, ]

    for year in range(1, years):
        future_value_avg = PersonalFinance.compound(principal, rate_avg, year, contribution)
        future_value_low = PersonalFinance.compound(principal, rate_low, year, contribution)
        future_value_high = PersonalFinance.compound(principal, rate_high, year, contribution)
        rand_rate = random.normalvariate(sp_mean, sp_std)
        future_value_rand = PersonalFinance.compound(data[-1]["Random Return"], rand_rate, 1, contribution)

        print("After {} year(s), you will have ${:.2f} saved. (rand={})".format(year, future_value_avg, rand_rate))
        data.append({"year": year,
                     "Average Return": future_value_avg,
                     "Low Return": future_value_low,
                     "High Return": future_value_high,
                     "Random Return": future_value_rand})

    df = pd.DataFrame(data)
    print(df)
    ax = df.plot.line(x="year", y=["Average Return", "Low Return", "High Return", "Random Return"],
                      figsize=(10, 4.25), title="Projected returns on investments", grid=True)
    ax.yaxis.set_major_formatter('${x:,.2f}')
    plt.show()


if __name__ == "__main__":
    main()
