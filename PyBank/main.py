#Your task is to create a Python script that analyzes the records 
#to calculate each of the following:
#The average change in "Profit/Losses" between months over the entire period
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
    for x in range(42)
        print(x)
    
    print("Finanacial Analysis")
    print("----------------------------")
    print(f"Total Months:{total_months}" )
    print(f"Total:{revenue}")
#The total number of months included in the dataset
#Financial Analysis
 # ----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
