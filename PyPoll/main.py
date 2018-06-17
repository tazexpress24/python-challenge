# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv


csvpath = os.path.join('election_data.csv')

total_votes = 0
#totalNetAmount = 0
#profit_loss = 0
#increasepercent = 0
#decreasepercent = 0
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
    #The total number of votes cast
    # Calculate the total number of votes   
     #   total_votes = total_months + 1
    #The total net amount of "Profit/Losses" over the entire period
     #   totalNetAmount = totalNetAmount + int(row[1])
    #The average change in "Profit/Losses" between months over the entire period
    #Average change in profit_loss = (Amount of last row - Amount of first row) / (Total length - 1)
       # Average change in profit_loss = (Amount of last row - Amount of first row)
    #The greatest increase in profits (date and amount) over the entire period.
    #First work the diff(increase = New num - Orig Num) between the two number
    #Then divide the increase by the orig num and multiply the answer by 100
    # % increase = Increase / Orig Num x 100
       # def increasepercent(num1, num2):
        #    num1 = float(num1)
        #    num2 = float(num2)
        #    percentage = '{0:.2f}'.format((num1 / num2 * 100))
        #    return increasepercentage
    #The greatest decrease in losses (date and amount) over the entire period    
    #First work out the diff (decrease = Orig num - New num) between the two numbers comparing
    #Then divide the decrease by the orig num and multiply the answer by 100
    # % decrease = Decrease / Orig Num x 100
   # Greatest Increase in Profits = 
       # def decreasepercent(num1,num2)
       #     return((float(num1) - num2) / abs(num2)) *100.00
            
    #print("Election Results")
    #print("----------------------------")
    #print(f"Total Votes Cast:{}" )
    #print(f"List Received Votes:{}")
    #print(f"Percent of Votes:{}")
    #print("Total Votes Candidate won:{}")
   # print("Winner:{}")


#Election Results
 # -------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
