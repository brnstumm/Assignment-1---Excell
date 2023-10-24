# set up def
import os
import csv

#setting the path of the file
csvpath = os.path.join('Resources','budget_data.csv')
file_to_output = "budget_analysis.txt"

# Creating lists to be used for calculations
fields = []
rows = []

#open a readable file to extract data and set starting values
with open(csvpath, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    total = 0
    plchange = 0
    max_giprofits = 0
    giprofitsdate = -1
    greatest_increase = 0
    gdprofitsdate = -1
    greatest_decrease = 0
    changevalues=[]
    gip_change_list=[]
    month_of_change=[]
    
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
        total += int(row[1])
        difference = int(row[1]) - plchange
        plchange = int(row[1])
        changevalues.append(difference)
        month_of_change += [row[0]]
           
 # Calculate the greatest increase
        if difference > greatest_increase:
            giprofitsdate = row[0]
            greatest_increase = difference

 # Calculate the greatest decrease       
        if difference < greatest_decrease:
            gdprofitsdate = row[0]
            greatest_decrease = difference

# Calculations for total months, net total amount, and the average change
    changevalues=changevalues[1:]
    Averagechange = sum(changevalues)/len(changevalues)    
    averagechangeround = round(Averagechange, 2)


# Printing out the results
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: %d"%(csvreader.line_num - 1))
    print("Total: $%d"%(total))
    print(f"Average change: ${averagechangeround}")
    print(f"Greatest Increase in Profits: {giprofitsdate} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {gdprofitsdate} (${greatest_decrease})")

#Write/export the results to a txt file
# save the output file path
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis \n")
    txt_file.write("-----------------------------------\n")
    txt_file.write("Total Months: %d\n"%(csvreader.line_num - 1))
    txt_file.write("Total: $%d\n"%(total))
    txt_file.write(f"Average change: ${averagechangeround}\n")
    txt_file.write(f"Greatest Increase in Profits: {giprofitsdate} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {gdprofitsdate} (${greatest_decrease})\n")
