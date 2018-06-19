import os

# Module for reading CSV's
import csv


csvpath = os.path.join('election_data.csv')

#Define the variables
totalvotes = 0
percent_votes = 0
votes = []
counties =  []
candidates = []
candidates_list = []
candidates

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        vote = int(row[0])
        votes.append(vote)

    
    #The total number of votes cast
        totalvotes = sum(votes)
    
    #A complete list of candidates who received votes
    for row in csvreader:
         candidates = str(row[2])
         #candidates.append(candidates)
         candidates_list = len(str(row[2]))

    #The percentage of votes each candidate won
    #for row in csvreader:
     #   vote = int(row[0])
     #   votes.append(vote)
    
    #percent_votes = ((votes[0] / sum(votes))
        
    #percentage of votes = total number votes of candidate / overall total number of votes

    #The total number of votes each candidate won
  
    for candidate_number in range(candidates):
   # print('Candidate {0}:'.format(candidate_number + 1))
    #name = input('Whats the name of this candidate?\n')
        candidate_info = (candidate_number + 1, name)
        candidates.append(candidate_info) 

    #The winner of the election based on popular vote.  
    
  
      
            
print("Election Results")
print("----------------------------")
print(f"Total Votes Cast:{totalvotes}" )
print(f"List Received Votes:{candidates_list}")
#print(f"Percent of Votes:{percent_votes}")
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
