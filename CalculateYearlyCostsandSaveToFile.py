import csv
from pathlib import Path

def check_yes(x):
    return x.lower() == 'y' or x.lower() == 'yes'

def ask_for_cost_inputs():
    item_name = input('Item name: ')
    item_cost = input('Item cost: ')
    item_cost = item_cost.replace('$','')
    item_restock_time = input('Restock every (number + days/weeks/months/years): ')
    item_restock_time_list = item_restock_time.split(' ')
    number_restock = item_restock_time_list[0]
    return item_name, item_cost, item_restock_time, number_restock

def caculate_yearly_costs():
    if item_restock_time.find('day') != -1:
        yearly_cost = float(item_cost) / float(number_restock) * 365
    if item_restock_time.find('week') != -1:
        yearly_cost = float(item_cost) / float(number_restock) * 52
    if item_restock_time.find('month') != -1:
        yearly_cost = float(item_cost) / float(number_restock) * 12
    if item_restock_time.find('year') != -1:
        yearly_cost = float(item_cost) / float(number_restock)
    yearly_cost = format(yearly_cost, '.2f')
    return yearly_cost

if __name__ == '__main__':
    caculate_more = True
    while caculate_more:
        item_name, item_cost, item_restock_time, number_restock = ask_for_cost_inputs()
        yearly_cost = caculate_yearly_costs()
        print(item_name + ' : $' + str(yearly_cost) + ' every year\n')
        save_file = input('Add to Yearly Cost text file? (Y/N) >> ')
        if check_yes(save_file):
            with open('Yearly Cost.txt', 'a') as save:
                save.write(item_name + ' : $' + str(yearly_cost) + '\n')
            
        save_file = input('Add to Yearly Cost csv file? (Y/N) >> ')
        if check_yes(save_file):
            csv_file = Path('Yearly Cost.csv')
            if csv_file.exists():
                with open('Yearly Cost.csv', 'a',newline='') as save:
                    writer = csv.writer(save)
                    writer.writerow([item_name, yearly_cost, item_cost, item_restock_time])
            else:
                with open('Yearly Cost.csv', 'a',newline='') as save:
                    writer = csv.writer(save)
                    writer.writerow(['Item Name', 'Yearly Cost', 'Item Cost','Item Buy Frequency'])                
                    writer.writerow([item_name, yearly_cost, item_cost, item_restock_time])
            
        caculate_more_question = input('Caculate another item? (Y/N) >> ')
        print()
        if not check_yes(caculate_more_question):  
            caculate_more = False
