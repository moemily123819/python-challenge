#
# author - Emily Mo
# date - Feb 3, 2019
# course - bootcamp U Miami Data Analytics
#
#  with input file election_data.csv, produce the following analysis :
#
# TThe total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
#
# Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#
#
#
import os
import csv
import operator
#
#

candidates=[]
output_lines=[]
total=[]
vote_percent[]
vote_results[]

def search_candidate(candidate):
    c = (candidates.index(candidate))
    candidates.append(candidate)
    total[c] = total[c] + 1
    


input_file = os.path.join('election_data.csv')
with open(input_file, 'r', newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter =',')
    csv_header = next(csvreader)


# Read each row of data after the header    
    for row in csvreader:
        search_candidate(row[3])

total_votes = sum(vote for vote in total)

# 
# calculate the percentage of each candidate 
#

for i in range(0, len(candidates)-1):
    vote_percent.append(float(total[i]) /total_votes)


#
# zip all the info - candidate + vote_percent + total 
#
# #

vote_results = zipper[vote_percent, candidate, total]

vote_results.sort(key=operator.itemgetter(1))

#
# format the election analysis into a list
#


output_lines.append('Election Results')
output_lines.append('----------------------------')
output_lines.append(f'Total Votes : {total_votes}')
output_lines.append('----------------------------')
for i in range(0, len(vote_results)-1):
    candidate = vote_results[1]
    output_lines.append(f'{vote_results(1)} : {vote_results[0]} ({long(vote_results[2]})')
output_lines.append('----------------------------')
output_lines.append(f'Winner : {vote_results[int(total)}')
output_lines.append(f'Average Change : ${avgChanges}')
output_lines.append(f'Greatest Increase in Profits: {dateRec[greatestInd+1]} (${int(bigChanges[1])})')
output_lines.append(f'Greatest Decrease in Profits: {dateRec[leastInd+1]} (${int(bigChanges[3])})')


for outputlines in output_lines:
    print(outputlines)

output_file = os.path.join('budget_output.csv')

with open(output_file, 'w') as budget_output_file:
    for outputlines in output_lines:
        budget_output_file.write(outputlines + '\n')