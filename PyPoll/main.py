import os

# Module for reading CSV's
import csv


csvpath = os.path.join('election_data.csv')

#Define the variables
totalvotes = 0
percent_votes = 0
votes = []
candidates = []
votesPerCandidate = []
largest_so_far = 0
winner = 0
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
        candidate = str(row[2])

        isNewCandidate = 1
        for i in range(0, len(candidates)):
            if candidate == candidates[i]:
                isNewCandidate = 0
                votesPerCandidate[i] += 1
        
        if isNewCandidate == 1:
            candidates.append(candidate)
            votesPerCandidate.append(1)
    #The total number of votes cast
        totalvotes += 1
            
    #percentage of votes = total number votes of candidate / overall total number of votes

    #The total number of votes each candidate won
  
    # for candidate_number in range(0, len(candidates) - 1):
   # print('Candidate {0}:'.format(candidate_number + 1))
    #name = input('Whats the name of this candidate?\n')
        # candidate_info = (candidate_number + 1, name)
        # candidates.append(candidate_info) 

    #The winner of the election based on popular vote.  
    # for i in range(int(votes[0])):
    #     if candidate_number > largest_so_far:
    #         largest_so_far = i 
    #         print(largest_so_far, i)
  
      
            
print("Election Results")
print("----------------------------")
for i in range(0, len(candidates)):
    percent = votesPerCandidate[i] / totalvotes
    print(f"{candidates[i]} : {percent} ({votesPerCandidate[i]})")

    if(votesPerCandidate[winner] < votesPerCandidate[i]):
        winner = i




print(f"Total Votes Cast:{totalvotes}" )
print(f"List Received Votes:{candidates}")
print("----------------------------")
print(f"Winner : {candidates[winner]}" )
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
