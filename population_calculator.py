population = float(input("Enter the current world population: "))
growth_rate = float(input("Enter the annual world population growth rate (%): "))

growth_rate = growth_rate / 100

population1 = population * (1 + growth_rate)
population2 = population1 * (1 + growth_rate)
population3 = population2 * (1 + growth_rate)
population4 = population3 * (1 + growth_rate)
population5 = population4 * (1 + growth_rate)

print("\nEstimated World Population:")
print("Population after 1 year: {:.0f}".format(population1))
print("Population after 2 years: {:.0f}".format(population2))
print("Population after 3 years: {:.0f}".format(population3))
print("Population after 4 years: {:.0f}".format(population4))
print("Population after 5 years: {:.0f}".format(population5))
