from PersonalFinance import PersonalFinance

principal = 10000.00
contribution = 1000.00
years = 10
rate = .08

print("You are starting with ${:.2f}, contributing ${:.2f} annually. Your average rate of return is {:.2%}".format(
	principal, contribution, rate))

for year in range(1, years):
	future_value = PersonalFinance.PersonalFinance.compound(principal, rate, year, contribution)
	print("After {} year(s), you will have ${:.2f} saved.".format(year, future_value))
