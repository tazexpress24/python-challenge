#Your task is to create a Python script that analyzes the records 
#to calculate each of the following:
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal 
#Import the file
#export a text file with the results.
#What records do I want
#Open the record
#Analyze the record
#Sort through the record
#Retreive the data from the columns
#Get the sum of the total number of months
#Get the total of Profit/losses over the entire period
#Average the change in Profit/losses between months over the entire period
#Calculate the higest increase of Profit (date&amount) over entire period
#Cal the higest decrease in losses (date&amount) over entire period
#Final script should print the analysis to the terminal

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv


csvpath = os.path.join('budget_data.csv')

total_months = 0
totalNetAmount = 0
profit_loss = 0
increasepercent = 0
decreasepercent = 0
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
    #The total number of months included in the dataset    
        total_months = total_months + 1
    #The total net amount of "Profit/Losses" over the entire period
        totalNetAmount = totalNetAmount + int(row[1])
    #The average change in "Profit/Losses" between months over the entire period
    #Average change in profit_loss = (Amount of last row - Amount of first row) / (Total length - 1)
       # Average change in profit_loss = (Amount of last row - Amount of first row)
    #The greatest increase in profits (date and amount) over the entire period.
    #First work the diff(increase = New num - Orig Num) between the two number
    #Then divide the increase by the orig num and multiply the answer by 100
    # % increase = Increase / Orig Num x 100
        def increasepercent(num1, num2):
            num1 = float(num1)
            num2 = float(num2)
            percentage = '{0:.2f}'.format((num1 / num2 * 100))
            return increasepercentage
    #The greatest decrease in losses (date and amount) over the entire period    
    #First work out the diff (decrease = Orig num - New num) between the two numbers comparing
    #Then divide the decrease by the orig num and multiply the answer by 100
    # % decrease = Decrease / Orig Num x 100
   # Greatest Increase in Profits = 
       # def decreasepercent(num1,num2)
       #     return((float(num1) - num2) / abs(num2)) *100.00
            
    print("Finanacial Analysis")
    print("----------------------------")
    print(f"Total Months:{total_months}" )
    print(f"Total:{totalNetAmount}")
    #print(f"Average Change:{}")
    print("Greatest Increase in Profits:{increasepercent}")
   # print("Greatest Decrease in Profits:{decreasepercent}")

#Financial Analysis
 # ----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
