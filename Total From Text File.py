total = 0.00
total = format(total, ".2f")
with open("Yearly Cost.txt") as file:
    for line in file:
        line_list = line.split("$")
        line_amount = line_list[1].replace('\n', '')
        line_amount = float(line_amount)
        total = float(total) + line_amount
print("Yearly Total: $" + str(total))
file.close()
