import os
import csv
# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as file:
    csv_reader = csv.reader(file, delimiter=',')
    csv_header = next(csv_reader)

   # print(f"CSV Header: {csv_header}")
    f"Financial Analysis"
    print("Financial Analysis")
    f""
    print("")

    f"---------------------------------------------"
    print("-----------------------------------")
    #creating an Arrary
    numbers = []
    month = []
    for row in csv_reader:
        numbers.append(int(row[1]))
        month.append(row[0])
    list(map(int,numbers))
        #print(numbers)
        
    #Total Months
    periodmonths = len(numbers)
    print("Total Months: ",periodmonths)

    # total of P&L
    totalnumber = sum(numbers)
    print("Total:   $",totalnumber)

    #creating Array
    changes = []
    changes = [numbers[i + 1] - numbers[i] for i in range(len(numbers)-1)]
    #print(changes)

    #Average changes
    Average_Change = sum(changes) / len(changes)
    Average_Change = round(Average_Change,2)
    print("Average Change:",  "$",Average_Change)

    #Greatest Increase in Profits
    GIP = max(changes)
    GIP_Max_Index = changes.index(GIP)
    GIP_Month = month[GIP_Max_Index+1]
    #print(GIP_Month)
    print(f"Greatest Increase in Profits: {GIP_Month} (${GIP})")

    GIP_Max_Index = changes.index(GIP)
    #print (GIP_Max_Index)

    #max
    GIP_Main_Index = GIP_Max_Index - 1
    #print(GIP_Main_Index)
    #print(list(csv_reader))
    #print("numbers",numbers[GIP_Main_Index])

    #Greatest Decrease in Profits
    GID = min(changes)
    GID_Min_Index = changes.index(GID)
    GID_Month = month[GID_Min_Index+1]
    print(f"Greatest Decrease in Profits: {GID_Month}  (${GID})")

#output file
# Specify the file to write to
#output_path = os.path.join("analysis",  "Financial Analysis.txt")
with open ('analysis.txt','w') as txt:
    txt.write("Financial Analysis\n")
    txt.write(f"---------------------------------------------\n")
    txt.write(f"Total Months: {periodmonths}\n")
    txt.write(f"Total:  ${totalnumber}\n")
    txt.write(f"Average Change: ${Average_Change}\n")
    txt.write(f"Greatest Increase in Profits: {GIP_Month} (${GIP})\n")
    txt.write(f"Greatest Decrease in Profits: {GID_Month} (${GID})")
