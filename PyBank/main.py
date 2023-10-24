#Import OS and CSV read file
import os
import csv
#Give CSV a path
budget_csv = os.path.join('PyBank','Resources' , 'budget_data.csv')
#Define
months_total = []
profits = []
months = []
monthly_change = 0
number = 0
#Read CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    total = 0
#Get count for total number of months
    for row in csvreader:
        months_total.append(row[0])
#Find the monthly changes in profit
        monthly_change = int(row[1])-number
        profits.append(monthly_change)
        number = int(row[1])

#Find the greatest increase
    greatest_increase = max(profits)
 
#Find the greatest loss
    greatest_loss = min(profits)
#Calculate average monthly change
    average_profit_change = sum(profits)/len(profits)
#Get Net Total of profits and losses
with open(budget_csv) as fin:
    header = next(fin)
    monthly_profit = 0
    for row in csv.reader(fin):
        monthly_profit += int(row[1])



#Print Statements
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(months_total)}")
print(f"Total: ${monthly_profit}") 
print(f"Average Change: ${average_profit_change}")
print(f"Greatest Increase in Profits: ${greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_loss}")

