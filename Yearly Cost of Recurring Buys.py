# Write your code here :-)
item_name = input('Item name: ')
item_cost = input('Item cost: ')
item_restock_time = input('Restock every (number + days/weeks/months/years): ')
item_restock_time_list = item_restock_time.split(" ")
number_restock = item_restock_time_list[0]
if item_restock_time.find("day") != -1:
    yearly_cost = float(item_cost) / float(number_restock) * 365
if item_restock_time.find("week") != -1:
    yearly_cost = float(item_cost) / float(number_restock) * 52
if item_restock_time.find("month") != -1:
    yearly_cost = float(item_cost) / float(number_restock) * 12
if item_restock_time.find("year") != -1:
    yearly_cost = float(item_cost) / float(number_restock)
yearly_cost = format(yearly_cost, '.2f')
print(item_name + " : $" + str(yearly_cost) + " every year\n")
save_file = input("Save to text file? (Y/N) >> ")
if save_file == "Y" or save_file == "y":
    with open('Yearly Cost.txt', "a") as save:
        save.write(item_name + " : $" + str(yearly_cost) + "\n")
    save.close()
