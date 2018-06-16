#First import the os module
#This will allow us to create file paths across operating systems
import os

#Module for reading csv's
import csv

csvpath = os.path.join(' election_data.csv')

total_votes = 0
with open(csvpath, newline='') as csvfile:

    #csv reader specifices delimiter and variable that holds content
    csvreader = csv.reader(csvfile,delimiter=',')

    print(csvreader)

    #Read the header row first(skip this step if there is now header)

    csv_header = next(csvreader)
#Read each row of data after the haeder
for row in csvreader:

    total_votes = total_votes + 1

print("Election Results")
print("-------------------------")
print(f"Total Votes:{total_votes}" )

 #Election Results
#-------------------------
 # Total Votes: 3521001
 # -------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------


    