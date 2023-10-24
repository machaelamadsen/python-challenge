#Import OS and CSV read file
import os
import csv
#Give CSV a path
election_csv = os.path.join('PyPoll','Resources' , 'election_data.csv')
#Define Lists 
total_votes = []
candidates_results = []
candidates = []

#Read CSV File
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
#count total number of votes
    for row in csvreader:
        total_votes.append(row[0])
        candidates.append(row[2])

#List each candidate
    candidate_options = row[2]
    if candidate_options not in candidates_results:
        candidate_options = set(candidates)
   


#Print Results
print("Election Results")
print("-----------------------------")
print(f'Total Votes: {len(total_votes)}')
print("-----------------------------")
print(candidate_options)
print("-----------------------------")
print("Winner:")
print("-----------------------------")

#Export as Text File
output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Election Results\n")
    new.write("-----------------------------\n")
    new.write(f'Total Votes: {len(total_votes)}\n')
    new.write(f"-----------------------------\n")
    new.write(f'{candidate_options}\n')
    new.write("-----------------------------\n")
    new.write("Winner:\n")
    new.write("-----------------------------\n")
