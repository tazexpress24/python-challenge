import os
import csv
csvpath = os.path.join('election_data.csv')
#Defining the function
def getPercentages(inputPLayerList):
    print(inputPLayerList)
    nameToCheck = inputPLayerList[0]
    wins = inputPLayerList[1]
    loss = inputPLayerList[2]
    draws = inputPLayerList[3]
    totalMatches = int(wins) + int(loss) + int(draws)
    percentageWon = float(wins) / float(totalMatches)
    percentageLost = float(loss) / float(totalMatches)
    percentageDraw = float(draws) / float(totalMatches)
print("PLAYER ANALYSIS")
print("-------------------------------------------")
#print("Player Name: " + name)
#print("Matches Won: " + wins)
#print("Matches Lost: " + loss)
#print("Matches Draw: " + draws)
#print("Percentage Won: " + "{:.2%}".format(percentageWon))
#print("Percentage Won: " + "{:.2%}".format(percentageLost))
#print("Percentage Won: " + "{:.2%}".format(percentageDraw))
#print("-------------------------------------------")
#Read in the CSV file
with open(csvpath, newline='') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

       # Loop through the data
    for row in csvreader:
