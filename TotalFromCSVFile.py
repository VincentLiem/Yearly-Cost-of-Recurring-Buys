import csv

def caculate_and_print_from_year_total(year_total):
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

if __name__ == "__main__":
    try:
        year_total = 0.00
        with open('Yearly Cost.csv',) as file:
            read = csv.reader(file)
            row_reading = 0
            for row in read:
                if row_reading != 0:
                    row_amount = row[1]
                    year_total = float(year_total) + float(row_amount)
                    year_total = format(year_total, '.2f')
                row_reading += 1
        caculate_and_print_from_year_total(year_total)
    except FileNotFoundError:
        print("Yearly Cost.csv not created yet")
