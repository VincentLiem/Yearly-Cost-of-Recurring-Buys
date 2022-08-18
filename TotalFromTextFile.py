from TotalFromCSVFile import *
try:
    year_total = 0.00
    savefile = os.path.join("Output", "Yearly Cost.txt")
    with open(savefile) as file:
        for line in file:
            line_list = line.split('$')
            line_amount = line_list[1].replace('\n', '')
            year_total = float(year_total) + float(line_amount)
            year_total = format(year_total, '.2f')
    caculate_and_print_from_year_total(year_total)
except FileNotFoundError:
    print("Yearly Cost.txt not created yet")
