# import libraries
import csv
from pathlib import Path


# import csv file & store as variable
budget_csv = Path("03-Python_homework_assignment_PyBank_Resources_budget_data.csv")


# create empty lists as variables
total_months = []
total_profit = []
prof_change = []

# analysis of the csv
with open(budget_csv, newline = "", encoding = "utf-8") as budget:
    csvreader = csv.reader(budget, delimiter = ",")
    header = next(csvreader) # obtain the header of the csv file
    
    for row in csvreader:
        total_months.append(row[0]) # tracks the total amount of months and adds each month to the empty list created above
        total_profit.append(int(row[1])) # tracks the total profit and adds each row of profit to the empty list created above
    
    # track the month to month change in profit
    for i in range(len(total_profit)-1):
        prof_change.append(total_profit[i+1] - total_profit[i])

# find the maximum and the minimum monthly change in profit
max_prof_change = max(prof_change)
min_prof_change = min(prof_change)

# find the months in which the maximum and minimum change in profit occurs
max_increase_prof = prof_change.index(max_prof_change) + 1
min_increase_prof = prof_change.index(min_prof_change) + 1

# print statements to display necessary results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(prof_change)/len(prof_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_prof]} (${(str(max_prof_change))})") # total_months[max_increase_prof] takes the value found and returns the actual month
print(f"Greatest Decrease in Profits: {total_months[min_increase_prof]} (${(str(min_prof_change))})") # total_months[min_increase_prof] takes the value found and returns the actual month

# create an output .txt file to export the results to
output_file = Path("Financial_Analysis_Summary.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n") # new line
    file.write("--------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(prof_change)/len(prof_change), 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_prof]} (${(str(max_prof_change))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_increase_prof]} (${(str(min_prof_change))})")
