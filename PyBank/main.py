
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv


csvpath = os.path.join('budget_data.csv')

#Define the variables used
total_months = 0
totalNetAmount = 0
profit_loss = 0
greatestincreasepercent = 0
greatestdecreasepercent = 0
values = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        value = int(row[1])
        values.append(value)
       
    #The average change in "Profit/Losses" between months over the entire period
    #Average change in profit_loss = (Amount of last row - Amount of first row) / (Total length - 1)
    profit_loss = (values[0] - values[len(values) - 1]) / len(values)
    
    
    #The total number of months included in the dataset
    #The total months will be length of the dataset
    total_months = len(values)

    #The total net amount of "Profit/Losses" over the entire period
    #Sum the value in the dataset
    totalNetAmount = sum(values)


    #The greatest increase in profits (date and amount) over the entire period.
    #First work the diff(increase = New num - Orig Num) between the two number
    #Then divide the increase by the orig num and multiply the answer by 100
    # % increase = Increase / Orig Num x 100
    #The greatest decrease in losses (date and amount) over the entire period    
    #First work out the diff (decrease = Orig num - New num) between the two numbers comparing
    #Then divide the decrease by the orig num and multiply the answer by 100
    # % decrease = Decrease / Orig Num x 100

    for i in range(0, len(values) - 1):
        change = ((values[i] - values[i+1]) / values[i]) * 100

        if greatestincreasepercent < change :
            greatestincreasepercent = change

        if greatestdecreasepercent > change :
            greatestdecreasepercent = change

    print("Finanacial Analysis")
    print("----------------------------")
    print(f"Total Months:{total_months}" )
    print(f"Total:{totalNetAmount}")
    print(f"Average Change:{profit_loss}")
    print(f"Greatest Increase in Profits:{greatestincreasepercent}")
    print(f"Greatest Decrease in Profits:{greatestdecreasepercent}")

