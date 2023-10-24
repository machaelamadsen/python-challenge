#Import OS and CSV read file
import os
import csv
#Give CSV a path
election_csv = os.path.join('PyPoll','Resources' , 'election_data.csv')
#Define Lists and Dictionories
total_votes = []
candidate_votes = []
candidates_results = []
#Read CSV File
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
#count total number of votes
    for row in csvreader:
        total_votes.append(row[0])
#List each candidate
        candidate_options = row[2]
        if candidate_options not in candidates_results:
            candidate_options = row[2]
            
        
        
        

        



#Print Results
print("Election Results")
print("-----------------------------")
print(f'Total Votes: {len(total_votes)}')
print("-----------------------------")
print(candidate_options)
