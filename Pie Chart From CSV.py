import pandas
import matplotlib.pyplot
csv_file = pandas.read_csv ('Yearly Cost.csv')

item_name = csv_file['Item Name']
yearly_cost = csv_file['Yearly Cost']

matplotlib.pyplot.pie(yearly_cost, labels = item_name)
matplotlib.pyplot.title("Breakdown of costs")
matplotlib.pyplot.show()
