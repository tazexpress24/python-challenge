#Your task is to create a Python script that analyzes the records 
#to calculate each of the following:
#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal 
#Import the file
import os 
import csv
#export a text file with the results.
csvpath=os.path.join('..'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)


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

#Export a text file with the results