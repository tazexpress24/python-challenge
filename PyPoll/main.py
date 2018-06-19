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
winner = 0
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   
    #Read each row of data after the header
    for row in csvreader:
        vote = int(row[0])
        votes.append(vote)
        candidate = str(row[2])

    #Read the candidates on the list
    #Loop through the list to find each new candidate
    #Find the candidate and votes per each candidate
        isNewCandidate = 1
        for i in range(0, len(candidates)):
            if candidate == candidates[i]:
                isNewCandidate = 0
                votesPerCandidate[i] += 1
                
    #
        if isNewCandidate == 1:
            candidates.append(candidate)
            votesPerCandidate.append(1)


    #The total number of votes cast
        totalvotes += 1
  
            
print("Election Results")
print("----------------------------")

#percentage of votes = total number votes of candidate / overall total number of votes

for i in range(0, len(candidates)):
    percent = votesPerCandidate[i] / totalvotes
    print(f"{candidates[i]} : {percent} ({votesPerCandidate[i]})")

    if(votesPerCandidate[winner] < votesPerCandidate[i]):
        winner = i

print(f"Total Votes Cast:{totalvotes}" )
print(f"List Received Votes:{candidates}")
print("----------------------------")
print(f"Winner : {candidates[winner]}" )



