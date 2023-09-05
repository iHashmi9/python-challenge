import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")

totalmonths=0
nettotal=0
prevprofitloss=None
profitlosschanges=[]
date=[]

with open(filepath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        dates = row[0]
        profitloss = int(row[1])
        
        totalmonths += 1
        nettotal += int(row[1])
        
        if prevprofitloss != 0:
            change = profitloss - prevprofitloss
            profitlosschanges.append(change)
            dates.append(date)
            
        prevprofitloss = profitloss
        
avgchange = sum(profitlosschanges) / len(profitlosschanges)

greatestinc = max(profitlosschanges)
greatestincdate = dates[profitlosschanges.index(greatestinc)]

greatestdec = min(profitlosschanges)
greatestdecdate = dates[profitlosschanges.index(greatestdec)]

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {totalmonths}")
print(f"Average Change: ${round(avgchange, 2)}")
print(f"Greatest Increase in proficks: {greatestincdate} (${greatestinc})")
print(f"Greatest Decrease in proficks: {greatestdecdate} (${greatestdec})")

outputfile= "Analysis/financial_analysis.txt"
with open(outputfile, 'w') as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("------------------------")
    txtfile.write(f"Total Months: {totalmonths}")
    txtfile.write(f"Total: ${nettotal}")
    txtfile.write(f"Average Change: ${round(avgchange,2)}")
    txtfile.write(f"Greatest Increase in proficks: {greatestincdate} (${greatestinc})")
    txtfile.write(f"Greatest Decrease in proficks: {greatestdecdate} (${greatestdec})")
    
    txtfile.write("-------------------------")