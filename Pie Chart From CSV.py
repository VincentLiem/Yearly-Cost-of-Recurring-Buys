import pandas
import matplotlib.pyplot as pyplot
csv_file = pandas.read_csv ('Yearly Cost.csv')

item_name = csv_file['Item Name']
yearly_cost = csv_file['Yearly Cost']

pyplot.pie(yearly_cost, labels = item_name)
pyplot.title("Breakdown of Costs")
pyplot.show()
