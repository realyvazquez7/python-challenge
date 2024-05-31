import csv
import os

# Path to collect data from the Resources folder
election_data_csv = os.path.join(os.path.dirname(__file__), '..', 'Resources', 'election_data.csv')

# Initialize variables to store data
total_votes = 0
candidate_votes = {}

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment total votes
        total_votes += 1
        
        # Extract candidate name from the row
        candidate_name = row[2]
        
        # If candidate already exists in dictionary, increment their vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # If candidate is new, add them to the dictionary with 1 vote
        else:
            candidate_votes[candidate_name] = 1

# Save the results to a text file
output_path = os.path.join(os.path.dirname(__file__), '..', 'analysis', 'election_analysis.txt')
with open(output_path, 'w') as txtfile:
    # Write the analysis results to the text file
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    winner = max(candidate_votes, key=candidate_votes.get)
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
