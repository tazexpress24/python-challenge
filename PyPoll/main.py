import os

# Module for reading CSV's
import csv


csvpath = os.path.join('election_data.csv')

#votecnt = 0
#totalNetAmount = 0
#profit_loss = 0
#increasepercent = 0
#decreasepercent = 0
#  length = 0
votes = []
counties =  []
candidates = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        print(row)

    #The total number of votes cast
    #Calculate the total number of votes   
    #def NumCount(file)
     #   votecnt=0    
        #  for total_votes in file
        #   votecnt=votecnt+1
        #    return votecnt


    #A complete list of candidates who received votes
     #candidates = int[]
     #If candidates > 0:
    #    print(name of candidate)

    #The percentage of votes each candidate won
    #percentage of votes = total number votes of candidate / overall total number of votes

    #The total number of votes each candidate won
    # Function to find winner of an election where votes
# are represented as candidate names
#from collections import Counter
 
#def winner(input):
 
     # convert list of candidates into dictionary
     # output will be likes candidates = {'A':2, 'B':4}
     #votes = Counter(input)
      
     # create another dictionary and it's key will
     # be count of votes values will be name of 
     # candidates
     #dict = {}
 
     #for value in votes.values():
 
          # initialize empty list to each key to 
          # insert candidate names having same 
          # number of votes 
          #dict[value] = []
 
     #for (key,value) in votes.iteritems():
     #     dict[value].append(key)
 
     # sort keys in descending order to get maximum 
     # value of votes
     #maxVote = sorted(dict.keys(),reverse=True)[0]
 
     # check if more than 1 candidates have same 
     # number of votes. If yes, then sort the list
     # first and print first element
    #if len(dict[maxVote])>1:
    #     print sorted(dict[maxVote])[0]
    #else:
    #     print dict[maxVote][0]
 

    #The winner of the election based on popular vote.  
    
  
      
            
    #print("Election Results")
    #print("----------------------------")
    #print(f"Total Votes Cast:{votecnt}" )
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
