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

percentagevotes = {candidate: (votes / totalvotes) * 100 for candidate, votes in candidates.items()}

print("Election Results")
print("-----------------------")
print(f"Total Votes: {totalvotes}")
print("-----------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentagevotes[candidate]:.3f}% ({votes})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

outputfile = "Analysis/Election_Results.txt"
with open(outputfile, "w") as file:
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write("------------------------\n")
    for candidate, votes in candidates.items():
        file.write(f"{candidate}: {percentagevotes[candidate]:.3f}% ({votes})\n")
    file.write("------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
    
