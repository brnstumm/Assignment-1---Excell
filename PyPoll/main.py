import os
import csv

# Path to collect data from the resources folder and export data to text file
poll_csv = os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join("poll_analysis.txt")

# Declaration of necassary variables for calculations
vote_total = 0
candidate = ""
candidatelist = {}
winner_votes = 0
winner_name = ""
    
# Read the CSV file
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

# Row counter to calculate number of votes
    for row in csvreader:       
        vote_total +=1
        candidate = row[2]
        if candidate in candidatelist:
            candidatelist[candidate] += 1
        else:
            candidatelist[candidate] = 1

# For printing inital result in terminal (part 1)
print(f"```text")
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {vote_total}")
print(f"----------------------------")

# For printing in the text file part_1 (part 1)
part_1 = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {vote_total}\n"
    f"----------------------------\n"
    )
with open(file_to_output, "w") as txt_file:
    txt_file.write(part_1)
    
# For printing each candidates in format "name, percentage, votes"
for candidate in candidatelist:
    percentage = (candidatelist[candidate]/vote_total)*100
    percentage_formatted = "{:.3f}".format(percentage)
    print(candidate + ": " + str(percentage_formatted) + "%" + " (" + str(candidatelist[candidate]) + ")")
    
    part_2 = (f"{candidate} : {percentage_formatted}% ({candidatelist[candidate]})\n")

# calculate the number of votes and winner
    if candidatelist[candidate] > winner_votes:
        winner_votes = candidatelist[candidate]
        winner_name = candidate
    
    # Appending output file with results
    with open(file_to_output, "a") as txt_file:
        txt_file.write(part_2)

# For printing final part_3 (part 3)
part_3 = (
    f"----------------------------\n"
    f"Winner: {winner_name}\n"
    f"----------------------------\n"
    )
# Printing results in terminal
print(part_3)
# Appending output file
with open(file_to_output, "a") as txt_file:
    txt_file.write(part_3)
