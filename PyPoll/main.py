import os
import csv

csvfile = os.path.join("Resources", "election_data.csv")

totalvotes = 0
candidates ={}
winner = ""

with open(csvfile, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        totalvotes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
            
winner = max(candidates, key=candidates.get)
#that's a load of shit
#guy's shit too

percentagevotes = {candidate: (votes / totalvotes) * 100 for candidate, votes in candidates.items()}

print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentagevotes[candidate]:.3f}% ({votes})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

outputfile = "Analysis/election_results.txt"
with open(output_file, "w") as file:
    file.write("Election Results")
    file.write("------------------------")
    file.write(f"Total Votes: {totalvotes}")
    file.write("------------------------")
    for candidate, votes in candidates.items():
        file.write(f"{candidate}: {percentagevotes[candidate]:.3f}% ({votes})")
    file.write("------------------------")
    file.write(f"Winner: {winner}")
    file.write("-------------------------")
    
