import csv

year_total = 0.00
with open('Yearly Cost.csv') as file:
    read = csv.reader(file)
    for row in read:
        row_amount = row[1]
        year_total = float(year_total) + float(row_amount)
        year_total = format(year_total, '.2f')
month_total = float(year_total) / 12
month_total = format(month_total, '.2f')
week_total = float(year_total) / 52
week_total = format(week_total, '.2f')
day_total = float(year_total) / 365
day_total = format(day_total, '.2f')
print('Yearly Total: $' + str(year_total))
print('Monthly Total: $' + str(month_total))
print('Yearly Total: $' + str(week_total))
print('Daily Total: $' + str(day_total))
file.close()
