#
# author - Emily Mo
# date - Feb 2, 2019
# course - bootcamp U Miami Data Analytics
#
#  with input file budget_data.csv, produce the following financial data :
#
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
#
#  print the analysis on terminal as well as output it to a file - budget_output.csv
#
#
# Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#
#
import os
import csv

#
#  a function to find the greatest increase of profit between 2 months 
#  and the greatest decrease between 2 months
#  the index of where these are found are passed back to the main.py
#  the index will be used to locate the month 
#

def findExtreme(listOfNumbers):
    results=[]
    greatest = listOfNumbers[0]
    greatestInd = 0
    least = listOfNumbers[0]
    leastInd = 0

    for i in range(1, len(listOfNumbers)):
        if listOfNumbers[i] > greatest: 
            greatest = listOfNumbers[i]
            greatestInd = i
        if listOfNumbers[i] < least: 
            least = listOfNumbers[i]
            leastInd = i
    results.append(greatestInd)
    results.append(greatest)
    results.append(leastInd)
    results.append(least)
    return(results)
    


dateRec=[]
profit_loss=[]
output_lines=[]
difference=[]

input_file = os.path.join('../Resources', 'budget_data.csv')
with open(input_file, 'r', newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter =',')
    csv_header = next(csvreader)

# Read each row of data after the header    
    for row in csvreader:
        dateRec.append(row[0])
        profit_loss.append(row[1])

nbrOfMonths = len(dateRec)
total = 0.0
total = sum(float(figure) for figure in profit_loss)

# 
# calculate the difference between 2 months 
#

for i in range(1, len(profit_loss)):
    difference.append(float(profit_loss[i]) - float(profit_loss[i-1]))


#
# averageChanges is to find the accumulated total of the differences / number of months
#
# avgChanges is same as averageChanges except it has only 2 dec places
#

averageChanges = sum(difference) / len(difference)   
avgChanges= round(averageChanges, 2) 

#
# format the financial analysis into a list
#

bigChanges = []
bigChanges = findExtreme(difference)
greatestInd = int(bigChanges[0])
leastInd = int(bigChanges[2])
output_lines.append('Financial Analysis')
output_lines.append('----------------------------')
output_lines.append(f'Total Months : {len(dateRec)}')
output_lines.append(f'Total : ${int(total)}')
output_lines.append(f'Average Change : ${avgChanges}')
output_lines.append(f'Greatest Increase in Profits: {dateRec[greatestInd+1]} (${int(bigChanges[1])})')
output_lines.append(f'Greatest Decrease in Profits: {dateRec[leastInd+1]} (${int(bigChanges[3])})')


for outputlines in output_lines:
    print(outputlines)

output_file = os.path.join('../Resources/', 'budget_output.csv')

with open(output_file, 'w') as budget_output_file:
    for outputlines in output_lines:
        budget_output_file.write(outputlines + '\n')
         