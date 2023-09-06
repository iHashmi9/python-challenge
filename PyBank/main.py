import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")

totalmonths = 0
nettotal = 0
prevprofitloss = None
profitlosschanges = []
dates = []

with open(filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        date = row[0]
        profitloss = int(row[1])
        
        totalmonths += 1
        nettotal += profitloss

        if prevprofitloss is not None:
            change = profitloss - prevprofitloss
            profitlosschanges.append(change)
            dates.append(date)

        prevprofitloss = profitloss
        
avgchange = sum(profitlosschanges) / len(profitlosschanges)

greatestincrease = max(profitlosschanges)
greatestincreasedate = dates[profitlosschanges.index(greatestincrease)]

greatestdecrease = min(profitlosschanges)
greatestdecreasedate = dates[profitlosschanges.index(greatestdecrease)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${nettotal}")
print(f"Average Change: ${round(avgchange, 2)}")
print(f"Greatest Increase in Profits: {greatestincreasedate} (${greatestincrease})")
print(f"Greatest Decrease in Profits: {greatestdecreasedate} (${greatestdecrease})")

outputfile= "Analysis/Financial_Analysis.txt"
with open(outputfile, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${nettotal}\n")
    txtfile.write(f"Average Change: ${round(avgchange,2)}\n")
    txtfile.write(f"Greatest Increase in profits: {greatestincreasedate} (${greatestincrease})\n")
    txtfile.write(f"Greatest Decrease in profits: {greatestdecreasedate} (${greatestdecrease})\n")
    txtfile.write("-------------------------\n")