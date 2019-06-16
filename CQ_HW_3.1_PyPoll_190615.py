# Homework Tasks 
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

# Interface with OS and CSV
import os
import csv

# Import CSV
election_data_csv = os.path.join('..', "Resources", "election_data.csv")

# Lists to store data
Candidate = []
VoteCounter = []

# State variables
rowcount = 0
Winner = 0
WinnerName = ""
i = 0

# Open csv file
with open(election_data_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	# Skip header line
	next(csvreader)
	
    # Canidate & Vote Counter
	for row in csvreader:
		rowcount = rowcount + 1
		if row[2] not in Candidate:
			Candidate.append(row[2])
			VoteCounter.append(0)
		else:
			VoteCounter[Candidate.index(row[2])] = VoteCounter[Candidate.index(row[2])] + 1

# Select the winner with the highest vote count using 'len' function
Winner = max(range(len(VoteCounter)), key = lambda x: VoteCounter[x])
WinnerName = Candidate[int(Winner)]

# Reference line 2 thru 6 above
print("Election Results are in!")
print("--------------------------------------------")
print("Total Votes: " + str(rowcount))
print("--------------------------------------------")
while i <= (len(Candidate) - 1):
	print(Candidate[i] + ": " + str(round((VoteCounter[i]/rowcount * 100),2)) + "% (" + str(VoteCounter[i]) + ")")
	i = i + 1
print("--------------------------------------------")
print("Winner: " + str(WinnerName))
print("--------------------------------------------")

i = 0

# Write Text file
with open("Output.txt", "w") as output:
	output.write("Election Results are in!\n")
	output.write("--------------------------------------------\n")
	output.write("Total Votes: " + str(rowcount) + "\n")
	output.write("--------------------------------------------\n")
	while i <= (len(Candidate) - 1):
		output.write(Candidate[i] + ": " + str(round((VoteCounter[i]/rowcount * 100),2)) + "% (" + str(VoteCounter[i]) + ")\n")
		i = i + 1
	output.write("--------------------------------------------\n")
	output.write("Winner: " + str(WinnerName) + "\n")
	output.write("--------------------------------------------\n")